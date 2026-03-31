from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional, Tuple
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
    start_time: Optional[datetime] = None

    def is_high_priority(self) -> bool:
        """Return True if the task's priority is HIGH."""
        return self.priority == Priority.HIGH

    def mark_complete(self) -> Optional["Task"]:
        """Mark this task as completed. Returns a new Task if frequency is Daily."""
        self.completed = True
        if self.frequency == "Daily":
            next_time = self.start_time + timedelta(hours=24) if self.start_time else None
            return Task(
                title=self.title,
                duration_minutes=self.duration_minutes,
                priority=self.priority,
                pet=self.pet,
                frequency=self.frequency,
                start_time=next_time,
            )
        return None


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
        """Collect and sort all owner tasks by start_time (earliest first)."""
        all_tasks = self.owner.get_all_tasks()
        self.plan = sorted(
            all_tasks,
            key=lambda t: t.start_time or datetime.max
        )
        return self.plan

    def filter_by_pet(self, pet_name: str) -> List[Task]:
        """Return only tasks belonging to a specific pet."""
        return [t for t in self.plan if t.pet and t.pet.name == pet_name]

    def detect_conflicts(self) -> List[Tuple[Task, Task]]:
        """Return a list of (Task, Task) pairs whose scheduled times overlap."""
        conflicts = []
        timed = [t for t in self.plan if t.start_time is not None]
        for i, a in enumerate(timed):
            a_end = a.start_time + timedelta(minutes=a.duration_minutes)
            for b in timed[i + 1:]:
                if b.start_time < a_end:
                    conflicts.append((a, b))
        return conflicts

    def get_reasoning(self) -> str:
        """Return a human-readable explanation of the generated plan."""
        pass
