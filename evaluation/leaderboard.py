"""
Leaderboard system for comparing multiple agents.
"""


class Leaderboard:

    def __init__(self):
        self.results = []

    def add_result(self, agent_name, avg_reward):
        """
        Store result of an agent run.
        """
        self.results.append((agent_name, avg_reward))

    def display(self):
        """
        Display ranked leaderboard.
        """

        print("\nCustomer Support Agent Leaderboard")
        print("-----------------------------------")

        sorted_results = sorted(
            self.results,
            key=lambda x: x[1],
            reverse=True
        )

        for name, score in sorted_results:
            print(f"{name:<20} {score}")