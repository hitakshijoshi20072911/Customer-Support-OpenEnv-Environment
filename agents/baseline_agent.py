"""
Baseline Rule-Based Agent
"""

class BaselineAgent:

    def act(self, query):

        q = query.lower()

        if "refund" in q or "deducted" in q or "payment" in q:
            return "payment|high|initiate refund"

        elif "password" in q or "login" in q:
            return "account|medium|reset password"

        elif "cancel" in q or "subscription" in q:
            return "billing|medium|cancel subscription"

        elif "order" in q or "delivery" in q:
            return "order|medium|track order"

        else:
            return "general|low|contact support"