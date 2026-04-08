"""
Evaluation metrics for the Customer Support OpenEnv benchmark.
Now includes performance tracking by difficulty level.
"""


class MetricsCalculator:

    def __init__(self):

        self.total_tasks = 0
        self.total_reward = 0.0

        # Difficulty-based reward tracking
        self.easy_rewards = []
        self.medium_rewards = []
        self.hard_rewards = []

    def update(self, reward, difficulty):
        """
        Update metrics after each task evaluation.
        """

        self.total_tasks += 1
        self.total_reward += reward

        if difficulty == "easy":
            self.easy_rewards.append(reward)

        elif difficulty == "medium":
            self.medium_rewards.append(reward)

        elif difficulty == "hard":
            self.hard_rewards.append(reward)

    def compute(self):
        """
        Compute final benchmark metrics.
        """

        if self.total_tasks == 0:
            return {}

        avg_reward = self.total_reward / self.total_tasks

        easy_avg = sum(self.easy_rewards) / max(len(self.easy_rewards), 1)
        medium_avg = sum(self.medium_rewards) / max(len(self.medium_rewards), 1)
        hard_avg = sum(self.hard_rewards) / max(len(self.hard_rewards), 1)

        return {
            "tasks": self.total_tasks,
            "average_reward": round(avg_reward, 3),
            "easy_reward": round(easy_avg, 3),
            "medium_reward": round(medium_avg, 3),
            "hard_reward": round(hard_avg, 3)
        }