from env.environment import SupportEnv
from env.models import Action
from evaluation.metrics import MetricsCalculator
from agents.baseline_agent import BaselineAgent


class BenchmarkRunner:

    def __init__(self):
        self.env = SupportEnv()
        self.metrics = MetricsCalculator()
        self.agent = BaselineAgent()

    def run(self):

        print("\nAgent Performance Report")
        print("---------------------------")

        for task in self.env.tasks:

            observation = self.env.reset()

            done = False
            total_reward = 0

            while not done:

                response = self.agent.act(task.query)

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

            self.metrics.update(total_reward)

        results = self.metrics.compute()

        print(f"Tasks evaluated: {results['tasks']}")
        print(f"Average reward: {results['average_reward']}")
        print(f"Category accuracy: {results['category_accuracy']}")
        print(f"Priority accuracy: {results['priority_accuracy']}")


if __name__ == "__main__":
    runner = BenchmarkRunner()
    runner.run()