"""
models.py

Defines the structured Observation and Action models used by the RL environment.
"""

from pydantic import BaseModel


class SupportTask(BaseModel):
    """
    Represents a single customer support task.
    """
    id: int
    query: str
    history: str
    product: str
    category: str
    priority: str
    solution: str
    difficulty: str


class Action(BaseModel):
    """
    Action taken by the AI support agent.
    """

    category: str
    priority: str
    solution: str