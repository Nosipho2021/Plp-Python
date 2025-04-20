#!/usr/bin/env python3

# Advanced Calculator with Loop and Conditionals

print("🔢 Welcome to the Python Calculator!")

while True:
    # Get input from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("❌ Please enter valid numbers.")
        continue

    operation = input("Choose an operation (+, -, *, /): ")

    # Perform calculation
    if operation == "+":
        result = num1 + num2
        print(f"✅ {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"✅ {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"✅ {num1} * {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("❌ Error: Cannot divide by zero.")
            continue
        result = num1 / num2
        print(f"✅ {num1} / {num2} = {result}")
    else:
        print("❌ Invalid operation. Please use +, -, *, or /.")
        continue

    # Ask if the user wants to continue
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again != "yes":
        print("👋 Thanks for using the calculator. Goodbye!")
        break
