from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

PRIORITY_ORDER = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}


@dataclass
class Pet:
    name: str
    species: str
    owner_name: str
    tasks: List["Task"] = field(default_factory=list)

    def __str__(self) -> str:
        """Return a human-readable string representation of the pet."""
        return f"{self.name} ({self.species}) owned by {self.owner_name}"

    def add_task(self, task: "Task") -> None:
        """Append a task to this pet's task list."""
        self.tasks.append(task)


@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: Priority
    pet: Optional[Pet] = None
    completed: bool = False
    frequency: str = "Once"  # Options: "Once", "Daily", "Weekly"

    def is_high_priority(self) -> bool:
        """Return True if the task's priority is HIGH."""
        return self.priority == Priority.HIGH

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True
        if self.frequency == "Daily":
            print(f"Scheduling next occurrence for {self.title} tomorrow!")
            # In a real app, you'd create a duplicate task here


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return a flat list of all tasks across every owned pet."""
        return [task for pet in self.pets for task in pet.tasks]


class Scheduler:
    def __init__(self, owner: Owner, total_available_time: int):
        self.owner = owner
        self.total_available_time = total_available_time
        self.plan: List[Task] = []

    def generate_plan(self) -> List[Task]:
        """Collect and sort all owner tasks by priority (HIGH first)."""
        priority_map = {"high": 0, "medium": 1, "low": 2}
        all_tasks = self.owner.get_all_tasks()
        self.plan = sorted(
            all_tasks,
            key=lambda t: priority_map.get(t.priority.value, 3)
        )
        return self.plan

    def filter_by_pet(self, pet_name: str) -> List[Task]:
        """Return only tasks belonging to a specific pet."""
        return [t for t in self.plan if t.pet and t.pet.name == pet_name]

    def detect_conflicts(self) -> str:
        """Simple check: returns a warning if total task time exceeds available time."""
        total_task_time = sum(t.duration_minutes for t in self.plan)
        if total_task_time > self.total_available_time:
            return f"Warning: You have {total_task_time} mins of tasks but only {self.total_available_time} mins available!"
        return "No timing conflicts detected."

    def get_reasoning(self) -> str:
        """Return a human-readable explanation of the generated plan."""
        pass
