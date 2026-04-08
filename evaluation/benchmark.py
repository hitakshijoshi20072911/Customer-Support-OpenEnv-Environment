from env.environment import SupportEnv
from env.models import Action
from evaluation.metrics import MetricsCalculator
from agents.baseline_agent import BaselineAgent
from agents.llm_agent import LLMAgent
from evaluation.leaderboard import Leaderboard


class BenchmarkRunner:

    def __init__(self):

        self.env = SupportEnv()

        self.agents = {
            "Baseline Agent": BaselineAgent(),
            "LLM Agent": LLMAgent()
        }

        self.leaderboard = Leaderboard()

    def run(self):

        print("\nRunning Benchmark for All Agents")
        print("--------------------------------")

        for agent_name, agent in self.agents.items():

            print(f"\nEvaluating {agent_name}")

            metrics = MetricsCalculator()

            for task in self.env.tasks:

                observation = self.env.reset()

                done = False
                total_reward = 0

                while not done:

                    response = agent.act(task.query)

                    try:
                        category, priority, solution = response.split("|")
                    except:
                        category = "general"
                        priority = "medium"
                        solution = "contact support"

                    action = Action(
                        category=category.strip(),
                        priority=priority.strip(),
                        solution=solution.strip()
                    )

                    observation, reward, done, info = self.env.step(action)

                    total_reward += reward

                metrics.update(total_reward, task.difficulty)

            results = metrics.compute()

            print(f"Average Reward: {results['average_reward']}")

            self.leaderboard.add_result(agent_name, results["average_reward"])

        self.leaderboard.display()


if __name__ == "__main__":
    runner = BenchmarkRunner()
    runner.run()