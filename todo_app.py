import json

FILE = "todo_data.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

def add_task():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks()
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✔" if t["done"] else "❌"
        print(f"{i}. {t['title']} [{status}]")

def mark_done():
    view_tasks()
    num = int(input("Enter task number to mark done: "))
    if 1 <= num <= len(tasks):
        tasks[num-1]["done"] = True
        save_tasks()
        print("Task marked as done!")
    else:
        print("Invalid number")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        save_tasks()
        print("Task deleted!")
    else:
        print("Invalid number")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Bye 👋")
        break
    else:
        print("Invalid choice")
