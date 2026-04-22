def check_log():
    filename = input("Enter log file name: ").strip()

    try:
        with open(filename, "r") as file:
            found = False
            for line in file:
                if "ERROR" in line:
                    print(line.strip())
                    found = True

            if not found:
                print("No ERROR lines found.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' does not exist.")
