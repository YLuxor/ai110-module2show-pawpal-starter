# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Smarter Scheduling

The `Scheduler` class has been extended with the following features:

- **Priority sorting with a lambda** — `generate_plan()` uses an inline lambda and a `priority_map` dict to sort tasks HIGH → MEDIUM → LOW. Unknown priorities fall safely to the end.
- **Filter by pet** — `filter_by_pet(pet_name)` returns only the tasks belonging to a specific pet, preserving priority order from the generated plan.
- **Recurring tasks** — `Task` now has a `frequency` field (`"Once"`, `"Daily"`, `"Weekly"`). Calling `mark_complete()` on a daily task prints a reminder to schedule the next occurrence.
- **Conflict detection** — `detect_conflicts()` sums all task durations and warns if they exceed the owner's `total_available_time`.

# Testing PawPal+

Tests are written with **pytest** and live in `tests/test_pawpal.py`. Run them with:

```bash
pytest tests/
```

The test suite covers:

- Marking a task complete and verifying the `completed` flag flips ★★★★★
- Adding a task to a pet and confirming the task list grows ★★★★★
- Chronological ordering — `generate_plan()` sorts tasks by `start_time`, earliest first ★★★★☆
- Recurring daily tasks — completing a `"Daily"` task returns a new task scheduled exactly 24 hours later ★★★★☆
- **Scheduling overlap detection** — `detect_conflicts()` correctly identifies pairs of tasks whose times overlap, returning them as a list rather than a generic warning ★★★★★

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.
