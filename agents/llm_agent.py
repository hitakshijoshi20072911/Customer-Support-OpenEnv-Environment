"""
LLM Agent for Customer Support Environment
"""

import os
from openai import OpenAI


class LLMAgent:

    def __init__(self):

        self.client = OpenAI(
            base_url=os.getenv("API_BASE_URL"),
            api_key=os.getenv("OPENAI_API_KEY")
        )

        self.model = os.getenv("MODEL_NAME")

    def act(self, query):

        prompt = f"""
You are a customer support AI.

Classify the issue and propose a solution.

Format:
category|priority|solution

Customer Query:
{query}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content

        return output