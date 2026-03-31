from dataclasses import dataclass
from typing import List


@dataclass
class Pet:
    name: str
    species: str
    owner_name: str

    def __str__(self) -> str:
        pass


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str

    def is_high_priority(self) -> bool:
        pass


class Scheduler:
    def __init__(self, task_list: List[Task], total_available_time: int):
        self.task_list = task_list
        self.total_available_time = total_available_time

    def generate_plan(self) -> List[Task]:
        pass

    def get_reasoning(self) -> str:
        pass
