#Simple Calculator.py

choice = input("Select operation(+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result:.2f}")
elif choice == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result:.2f}")
elif choice == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result:.2f}")
elif choice == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print(f"Invalid {choice} operation selected.")