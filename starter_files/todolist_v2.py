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

def add_new_task(username):
    title = input("Task Title: ")
    status = input("Task Status: ")
    task_id = generate_unique_id()

    while status not in ['pending', 'in-progress', 'complete']:
        print('value for status must be "pending", "in-progress", or "complete"')
        status = input("Task Status: ")

    task = {
        "id": task_id,
        "title": title,
        "status": status
    }
    todos[username]['tasks'].append(task)
    display_task(username, task_id)

def update_task(username):
    task_id = input("Task ID: ")
    field = input("Field To Update: ")
    while field not in ['title', 'status']:
        print('field must be "title" or "status"')
        field = input("Field To Update: ")
    new_value = input("New Value: ")
    while field == "status" and new_value not in ['pending', 'in-progress', 'complete']:
        print('value for status must be "pending", "in-progress", or "complete"')
        new_value = input("New Value: ")

    task = get_task(username, task_id)
    if task is None: return
    task[field] = new_value
    display_tasks(username)

def delete_task(username):
    task_id = input('Task ID: ')
    if not get_task(username, task_id):
        return
    picked_index = None
    for idx, task in enumerate(todos[username]['tasks']):
        if task['id'] == task_id:
            picked_index = idx
            break
    todos[username]['tasks'].pop(picked_index)
    print("Task has been deleted successfully")

def init_program():
    username = input("Welcome! Please login: ")
    if username == "exit" or username == "cancel":
        print("Exiting the program.")
        exit()
    if username not in todos:
        print("User not found. Please try again.")
        return
    print("Available commands: ADD, UPDATE, DELETE, SHOW, LOGOUT")
    return username

command = None
username = None
while not username:
    username = init_program()

while command != "cancel" and command != "exit":
    command = input("Enter command: ")
    if command == "ADD":
        add_new_task(username)
    elif command == "UPDATE":
        update_task(username)
    elif command == "DELETE":
        delete_task(username)
    elif command == "SHOW":
        display_tasks(username)
    elif command == "LOGOUT":
        username = None
        while not username:
            username = init_program()

print("---------------------- See you soon!😀👋 ----------------------")