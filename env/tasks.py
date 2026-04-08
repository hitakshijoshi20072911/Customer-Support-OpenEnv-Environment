import json
from typing import List
from env.models import SupportTask


def load_tasks() -> List[SupportTask]:

    with open("data/tasks.json", "r") as f:
        raw_tasks = json.load(f)

    tasks = [SupportTask(**task) for task in raw_tasks]

    return tasks