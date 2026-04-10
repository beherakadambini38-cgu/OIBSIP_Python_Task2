
def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task Added ")
    save_tasks(tasks)

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("Your Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    idx = int(input("Enter task number to delete: "))
    if 0 < idx <= len(tasks):
        removed = tasks.pop(idx-1)
        print(f"Removed: {removed}")
        save_tasks(tasks)
    else:
        print("Invalid task number.")

tasks = load_tasks()

while True:
    print("\n1. Add Task  2. View Tasks  3. Delete Task  4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again!")
