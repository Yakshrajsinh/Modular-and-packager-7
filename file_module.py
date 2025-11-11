import os
from datetime import datetime

def file_operations():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to main menu")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            filename = input("Enter filename to create (with .txt extension): ")
            try:
                with open(filename, "x") as f:
                    f.write(f"File created on: {datetime.now()}\n")
                print(f"File '{filename}' created successfully.")
            except FileExistsError:
                print("File already exists!")

        elif choice == 2:
            filename = input("Enter filename to write to: ")
            content = input("Enter text to write: ")
            with open(filename, "w") as f:
                f.write(content)
            print(f"Content written to '{filename}' successfully.")

        elif choice == 3:
            filename = input("Enter filename to read: ")
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    print("\nFile Content:\n----------------")
                    print(f.read())
            else:
                print("File not found!")

        elif choice == 4:
            filename = input("Enter filename to append to: ")
            if os.path.exists(filename):
                content = input("Enter text to append: ")
                with open(filename, "a") as f:
                    f.write("\n" + content)
                print(f"Content appended to '{filename}' successfully.")
            else:
                print("File not found!")

        elif choice == 5:
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice! Please select 1–5.")

if __name__ == "__main__":
    file_operations()