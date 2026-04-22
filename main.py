from system_info import system_info
from log_checker import check_log
from task_manager import manage_tasks


def show_menu():
    print("\n=== Main Menu ===")
    print("[1] System Info")
    print("[2] Log Checker")
    print("[3] Task List")
    print("[0] Exit")


def main():
    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            system_info()
        elif choice == "2":
            check_log()
        elif choice == "3":
            manage_tasks()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
