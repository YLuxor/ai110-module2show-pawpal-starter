# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
ANS: Classes I included are: Pet for profile and Task for priority and duration_minutes
Responsibilities assigned are: Task class ensures validation of data enter 
Scheduler takes the lists of tasks from st.session_state to sort them based on owner's availability to create a daily schedule.

3 core actions 
Create pet profile, Build a Task queue, Create scheduling with daily tasks

List of Building Blocks
Class: Pet; Attributes: Name, species, owner_name; Methods: --str--
Class: Task; Attributes: title, duration_minutes, priority; Methods: is_high_priority()
Class: Scheduler; Attributes: task_list, total_available_time; Methods: generate_plan(), get_reasoning()


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
ANS: Yes, the design changed. Making a Task class. To make it easier when adding methods instead relying on raw key value pairs. 

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?
ANS:My scheduler primarily considers Total Available Time (to ensure the owner isn't overbooked) and Priority Level (Low, Medium, High).
I decided that Priority mattered most because, in pet care, certain tasks (like medication or feeding) are non-negotiable for the pet's health, whereas "Play" or "Grooming" can be moved if time runs out.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
ANS: My scheduler uses a "First-Fit" approach based on priority. It picks the highest priority tasks first until time runs out, rather than trying to fit the maximum number of small tasks into the schedule.
 In a pet care scenario, it is better to finish one high-priority 30-minute task (like a vet visit) than three 10-minute low-priority tasks (like brushing fur).
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I mostly used it for debugging and some startup brainstorming to see how to go about a step I don't fully understand. 
Some prompts like why is this failing? Update from this to this. 
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
ANS: When generating the Task class, the AI suggested a very complex time-parsing library. I chose to stay with a simple duration_minutes integer instead.
 I verified this by running a manual main.py test script. I realized the simpler integer approach made the math for the "Total Available Time" constraint much easier to read and debug.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
ANS: I tested Task Completion (ensuring the mark_complete method actually toggles the status) and Task Addition (ensuring the Pet's list grows when a task is added). They were important to keep the date reliable for the scheduler
**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
ANS: Moderate confidence I know there are some parts that are still not working the way I was expecting it to
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
ANS: I am most satisfied with the integration between the backend and Streamlit. Seeing the UI actually update the Owner object in the session state felt like a huge win.
**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
Working on this project taught me how things are done in the back end before having the user experience, how to implement new features, AI makes it a lot easier when it comes to brainstorming and debugging. 