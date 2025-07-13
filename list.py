tasks = []

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task description: ")
    tasks.append({"task": task, "done": False})
    print("✅ Task added.")

def view_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']} [{status}]")

def mark_done():
    view_tasks()
    try:
        i = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]["done"] = True
            print("✅ Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        i = int(input("Enter task number to delete: ")) - 1
        if 0 <= i < len(tasks):
            removed = tasks.pop(i)
            print(f"🗑️ Deleted: {removed['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice. Try again.")
