import math

def math_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        try:
            sub_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if sub_choice == 1:
            try:
                num = int(input("Enter a number: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    print(f"Factorial of {num} is {math.factorial(num)}")
            except ValueError:
                print("Please enter a valid integer.")

        elif sub_choice == 2:
            try:
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter annual interest rate (%): "))
                time = float(input("Enter time in years: "))
                comp = int(input("Enter number of times interest applied per year: "))

                amount = principal * (1 + (rate / 100) / comp) ** (comp * time)
                ci = amount - principal
                print(f"Compound Interest: {ci:.2f}")
                print(f"Total Amount: {amount:.2f}")
            except ValueError:
                print("Please enter valid numerical values.")

        elif sub_choice == 3:
            try:
                angle = float(input("Enter angle in degrees: "))
                rad = math.radians(angle)
                print(f"sin({angle}) = {math.sin(rad):.4f}")
                print(f"cos({angle}) = {math.cos(rad):.4f}")
                print(f"tan({angle}) = {math.tan(rad):.4f}")
            except ValueError:
                print("Invalid input! Enter a valid angle.")

        elif sub_choice == 4:
            print("\nChoose Shape:")
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")
            print("4. Square")

            shape = input("Enter choice: ")

            if shape == "1":
                r = float(input("Enter radius: "))
                print(f"Area of Circle = {math.pi * r**2:.2f}")
            elif shape == "2":
                l = float(input("Enter length: "))
                b = float(input("Enter breadth: "))
                print(f"Area of Rectangle = {l * b:.2f}")
            elif shape == "3":
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                print(f"Area of Triangle = {0.5 * base * height:.2f}")
            elif shape == "4":
                s = float(input("Enter side: "))
                print(f"Area of Square = {s * s:.2f}")
            else:
                print("Invalid shape choice.")

        elif sub_choice == 5:
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice! Please choose 1–5.")

if __name__ == "__main__":
    math_operations()