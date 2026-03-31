import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "owner" not in st.session_state:
    # Initialize our main data object
    st.session_state.owner = Owner("Xaden")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    # 1. Create a new Task object using your class
    new_task = Task(task_title, duration, priority)

    # 2. In a real app, you'd select which pet, but for now,
    # let's assume we add it to the first pet in our owner's list
    if not st.session_state.owner.pets:
        # Create a default pet if none exists so the app doesn't crash
        default_pet = Pet(pet_name, species, owner_name)
        st.session_state.owner.add_pet(default_pet)

    st.session_state.owner.pets[0].add_task(new_task)
    st.success(f"Added '{task_title}' to {st.session_state.owner.pets[0].name}'s list!")

all_tasks = st.session_state.owner.get_all_tasks()
if all_tasks:
    st.write("Current tasks:")
    st.table([{"title": t.title, "duration_minutes": t.duration_minutes, "priority": t.priority} for t in all_tasks])
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    scheduler = Scheduler(st.session_state.owner, total_available_time=120)
    plan = scheduler.generate_plan()

    if plan:
        st.table([
            {"title": t.title, "duration_minutes": t.duration_minutes, "priority": t.priority}
            for t in plan
        ])

        conflicts = scheduler.detect_conflicts()
        if conflicts:
            st.warning("⚠️ You have overlapping tasks!")
        else:
            st.success("No scheduling conflicts detected.")
    else:
        st.info("No tasks to schedule. Add some tasks above.")
