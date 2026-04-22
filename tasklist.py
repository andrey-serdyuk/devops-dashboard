def manage_tasks():
    tasks = []

    while True:
        print("\n=== Task Manager ===")
        print("[1] Add a task")
        print("[2] View all tasks")
        print("[3] Remove a task")
        print("[0] Return to main menu")

        choice = input("Select an option: ").strip()

        if choice == "1":
            task = input("Enter a new task: ").strip()
            if task:
                tasks.append(task)
                print("Task added.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                print("\nTasks:")
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue

            try:
                index = int(input("Enter task number to remove: ").strip())
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "0":
            break

        else:
            print("Invalid option, try again.")
