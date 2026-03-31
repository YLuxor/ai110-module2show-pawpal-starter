from pawpal_system import Task, Pet, Owner, Scheduler, Priority

# 1. Setup Data
my_owner = Owner("Xaden")
dog = Pet("Mochi", "Dog", "Jordan")
cat = Pet("Luna", "Cat", "Jordan")

my_owner.add_pet(dog)
my_owner.add_pet(cat)

# 2. Add Tasks
t1 = Task("Morning Walk", 20, Priority.HIGH)
t2 = Task("Feeding", 10, Priority.MEDIUM)
t3 = Task("Grooming", 30, Priority.LOW)

dog.add_task(t1)
dog.add_task(t3)
cat.add_task(t2)

# 3. Run Scheduler
# We'll assume the owner has 60 minutes available
scheduler = Scheduler(my_owner, 60)
plan = scheduler.generate_plan()

# 4. Print Output
print("--- Today's Schedule ---")
for task in plan:
    print(f"[{task.priority}] {task.title} - {task.duration_minutes} mins")