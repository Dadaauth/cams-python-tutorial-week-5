# Create a Todo-List CLI App 😀🔍
# Add, remove, show, and update tasks status
# Use a loop to make sure you continue asking for a user command until the user types and enters 'cancel' or 'exit'
# Don't Todo-List in files yet. Just use a convenient data structure

# Use the `display_tasks` and `display_task` functions to display all tasks or a single task

# To add a new task, use the command, ADD. then ask the user for the title and status of the task. i.e
# >>> ADD
# >>> Task Title: <user_input>
# >>> Task Status: <user_input>
# When creating new tasks, use the `generate_unique_id` function to automatically generate a unique id for each task
# Display the new task after adding it to the todo list in the specified format.

# To update tasks. Display all the tasks with their id then use the command
# UPDATE. Ask for these from the user: (1) <task_id> to work on. (2) <field> to update, i.e title or status
# (3) the new value to save
# i.e
# >>> UPDATE
# >>> Task ID: <user_input>
# >>> Field To Update: <user_input> 'title' or 'status'
# >>> New Value: <user_input>
# Display all tasks again after updating any value in any task

# To show / display tasks, use the command `SHOW` which will list all tasks with their id, title and status.
# Use the `display_tasks` function to achieve this

# To delete / remove tasks, use the command 'DELETE' then ask the user for the task id to delete. i.e
# >>> DELETE
# >>> Task ID: <user_input>
# If a task with the ID does not exist, show the user 'Task does not exist' else, show the user 'Task has been deleted successfully.'
# You can use the python built-in 'enumerate' function to find the index of the specific task you want to delete then use todos.pop(index)

# NOTE: All command names must be in uppercase, i.e. ADD, DELETE, UPDATE, SHOW.

# After Entering a command, Request the required data(s) from the user. i.e.
# >>> ADD
# >>> Task Title: <user_input>
# >>> Task Status: <user_input>

# Available task statuses (pending, in-progress, complete)

# Minimum Required Functions:
#   - add_new_task - to add a new task to the todo list 👍
#   - update_task - you know what it is 😐
#   - delete_task - you know what it is 😐

from uuid import uuid4

def generate_unique_id():
    # part of the starter file
    return str(uuid4())

# part of the starter file
todos = [
    {
        "id": generate_unique_id(),
        "title": "Work at Google",
        "status": "pending",
    },
    {
        "id": generate_unique_id(),
        "title": "Become an expert programmer",
        "status": "in-progress",
    },
    {
        "id": generate_unique_id(),
        "title": "Show up at CAMS AI tutorial today!",
        "status": "complete",
    }
]

def display_tasks():
    # part of the starter file
    for idx, task in enumerate(todos):
        print(f"{idx}. [{task['id']}] ({task['status']}): {task['title']}")

def get_task(task_id):
    # part of the starter file
    task = [task for task in todos if task['id'] == task_id]
    if len(task) == 0:
        print("Task does not exist")
        return
    task = task[0]
    return task

def display_task(task_id):
    # part of the starter file
    task = get_task(task_id)
    print(f"[{task['id']}] ({task['status']}): {task['title']}")

print("---------------------- Welcome to your Todo-List CLI APP 😀💻🚀 ----------------------")
# ... Your code goes here
# ...
# ...
# ...
# ...
# ...
# ...
# ...
# ... Your code goes here
print("---------------------- See you soon!😀👋 ----------------------")