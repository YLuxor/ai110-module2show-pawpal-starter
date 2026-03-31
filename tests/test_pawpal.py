import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler, Priority


def test_mark_complete():
    task = Task("Morning Walk", 20, Priority.HIGH)
    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_count():
    pet = Pet("Mochi", "Dog", "Jordan")
    assert len(pet.tasks) == 0
    task = Task("Feeding", 10, Priority.MEDIUM)
    pet.add_task(task)
    assert len(pet.tasks) == 1


# --- TDD tests: these define desired future behavior and will FAIL
# --- until pawpal_system.py is updated to support them.


def test_generate_plan_chronological_order():
    """generate_plan() should sort tasks by start_time, earliest first.
    Requires Task to gain a start_time: datetime field.
    """
    pet = Pet("Mochi", "Dog", "Jordan")
    t1 = Task("Evening Walk", 20, Priority.LOW,  start_time=datetime(2026, 3, 30, 18, 0))
    t2 = Task("Morning Feed", 10, Priority.HIGH, start_time=datetime(2026, 3, 30,  7, 0))
    t3 = Task("Noon Groom",   30, Priority.MEDIUM, start_time=datetime(2026, 3, 30, 12, 0))
    pet.add_task(t1)
    pet.add_task(t2)
    pet.add_task(t3)

    owner = Owner("Xaden")
    owner.add_pet(pet)
    scheduler = Scheduler(owner, 120)
    plan = scheduler.generate_plan()

    start_times = [t.start_time for t in plan]
    assert start_times == sorted(start_times), (
        "Tasks should be ordered earliest start_time first, regardless of priority"
    )


def test_daily_task_creates_new_task_24h_later():
    """Completing a Daily task should return a new Task scheduled 24 hours later.
    Requires:
      - Task gains a start_time: datetime field
      - mark_complete() returns the new Task (instead of printing and returning None)
    """
    start = datetime(2026, 3, 30, 8, 0)
    task = Task("Morning Walk", 20, Priority.HIGH, frequency="Daily", start_time=start)

    new_task = task.mark_complete()

    assert task.completed is True
    assert new_task is not None, "mark_complete() on a Daily task should return a new Task"
    assert new_task.completed is False, "The new task should not be pre-marked complete"
    assert new_task.title == task.title
    assert new_task.frequency == "Daily"
    assert new_task.start_time == start + timedelta(hours=24)


def test_detect_conflicts_returns_overlapping_tasks():
    """detect_conflicts() should return a list of (Task, Task) tuples that overlap.
    Two tasks overlap when the second one starts before the first one ends.
    Requires detect_conflicts() to return List[Tuple[Task, Task]] instead of a str.
    """
    pet = Pet("Mochi", "Dog", "Jordan")
    # t1: 08:00–08:30, t2: 08:15–08:35 → overlaps t1
    t1 = Task("Walk",  30, Priority.HIGH,   start_time=datetime(2026, 3, 30,  8,  0))
    t2 = Task("Feed",  20, Priority.MEDIUM, start_time=datetime(2026, 3, 30,  8, 15))
    # t3: 10:00–10:15 → no overlap
    t3 = Task("Groom", 15, Priority.LOW,    start_time=datetime(2026, 3, 30, 10,  0))
    pet.add_task(t1)
    pet.add_task(t2)
    pet.add_task(t3)

    owner = Owner("Xaden")
    owner.add_pet(pet)
    scheduler = Scheduler(owner, 120)
    scheduler.generate_plan()

    conflicts = scheduler.detect_conflicts()

    assert isinstance(conflicts, list), "detect_conflicts() should return a list, not a string"
    assert len(conflicts) == 1, "Exactly one overlapping pair expected"
    pair = conflicts[0]
    assert t1 in pair and t2 in pair, "The overlapping pair should be (Walk, Feed)"
