"""
Evaluation metrics for the Customer Support OpenEnv benchmark.
"""

class MetricsCalculator:

    def __init__(self):
        self.total_tasks = 0
        self.total_reward = 0.0
        self.correct_category = 0
        self.correct_priority = 0

    def update(self, reward, category_correct=False, priority_correct=False):
        """
        Update metrics after each task evaluation.
        """
        self.total_tasks += 1
        self.total_reward += reward

        if category_correct:
            self.correct_category += 1

        if priority_correct:
            self.correct_priority += 1

    def compute(self):
        """
        Compute final benchmark metrics.
        """

        if self.total_tasks == 0:
            return {}

        avg_reward = self.total_reward / self.total_tasks
        category_acc = self.correct_category / self.total_tasks
        priority_acc = self.correct_priority / self.total_tasks

        return {
            "tasks": self.total_tasks,
            "average_reward": round(avg_reward, 3),
            "category_accuracy": round(category_acc, 3),
            "priority_accuracy": round(priority_acc, 3)
        }