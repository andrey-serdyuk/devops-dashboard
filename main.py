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
            print("Coming soon...")
        elif choice == "2":
            print("Coming soon...")
        elif choice == "3":
            print("Coming soon...")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
