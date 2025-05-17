# Create a Todo-List CLI App 😀🔍
# Add, remove, show, and update tasks status

# Use the `display_tasks` and `display_task` functions to display all tasks or a single task

# Update the todolist to include a user login functionality

from uuid import uuid4

def generate_unique_id():
    # part of the starter file
    return str(uuid4())

# part of the starter file
todos = {
    "simon": {
        "tasks": [
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
    },
    "angel": {
        "tasks": [
            {
                "id": generate_unique_id(),
                "title": "Sleep at 9PM",
                "status": "pending",
            },
            {
                "id": generate_unique_id(),
                "title": "Wash some cloths",
                "status": "in-progress",
            },
            {
                "id": generate_unique_id(),
                "title": "Look Beautiful!",
                "status": "complete",
            }
        ]
    }
}

def display_tasks(username):
    # part of the starter file
    for idx, task in enumerate(todos[username]['tasks']):
        print(f"{idx}. [{task['id']}] ({task['status']}): {task['title']}")

def get_task(username, task_id):
    # part of the starter file
    task = [task for task in todos[username]['tasks'] if task['id'] == task_id]
    if len(task) == 0:
        print("Task does not exist")
        return
    task = task[0]
    return task

def display_task(username, task_id):
    # part of the starter file
    task = get_task(username, task_id)
    print(f"[{task['id']}] ({task['status']}): {task['title']}")

print("---------------------- Welcome to your Todo-List CLI APP 😀💻🚀 ----------------------")
# ... Your code goes here

# ... Your code goes here
print("---------------------- See you soon!😀👋 ----------------------")