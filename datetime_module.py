import time
from datetime import datetime

def datetime_operations():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate the difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to main menu")

        try:
            sub_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if sub_choice == 1:
            current = datetime.now()
            print("Current Date and Time:", current.strftime("%Y-%m-%d %H:%M:%S"))

        elif sub_choice == 2:
            print("Enter the first date/time (YYYY-MM-DD HH:MM:SS):")
            d1 = input("→ ")
            print("Enter the second date/time (YYYY-MM-DD HH:MM:SS):")
            d2 = input("→ ")
            try:
                date1 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
                date2 = datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
                diff = abs(date2 - date1)
                print(f"Difference: {diff.days} days, {diff.seconds // 3600} hours, {(diff.seconds % 3600) // 60} minutes")
            except ValueError:
                print("Invalid format! Please use YYYY-MM-DD HH:MM:SS")

        elif sub_choice == 3:
            print("Enter a date (YYYY-MM-DD):")
            date_input = input("→ ")
            try:
                date_obj = datetime.strptime(date_input, "%Y-%m-%d")
                print("Choose format:")
                print("1. DD/MM/YYYY")
                print("2. Month Day, Year (e.g., November 10, 2025)")
                print("3. Custom (Enter manually)")
                f_choice = int(input("Format choice: "))

                if f_choice == 1:
                    print("Formatted Date:", date_obj.strftime("%d/%m/%Y"))
                elif f_choice == 2:
                    print("Formatted Date:", date_obj.strftime("%B %d, %Y"))
                elif f_choice == 3:
                    custom = input("Enter your custom format (use %Y, %m, %d): ")
                    print("Formatted Date:", date_obj.strftime(custom))
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid date format!")

        elif sub_choice == 4:
            input("Press Enter to start the stopwatch...")
            start = time.time()
            input("Press Enter to stop the stopwatch...")
            end = time.time()
            elapsed = end - start
            print(f"Elapsed Time: {elapsed:.2f} seconds")

        elif sub_choice == 5:
            try:
                seconds = int(input("Enter countdown time in seconds: "))
                for i in range(seconds, 0, -1):
                    print(f"Time left: {i} seconds", end="\r")
                    time.sleep(1)
                print("\nTime’s up!")
            except ValueError:
                print("Please enter a valid number!")

        elif sub_choice == 6:
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice! Please select from 1–6.")

if __name__ == "__main__":
    datetime_operations()