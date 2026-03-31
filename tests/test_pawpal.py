import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Task, Pet, Priority


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
