# Basic Ahh Calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2st number: "))

if operator == "+":
    result = num1 + num2
    print(result, 3)
elif operator == "-":
    result = num1 - num2
    print(result, 3)
elif operator == "*":
    result = num1 * num2
    print(result, 3)
elif operator == "/":
    result = num1 / num2
    print(result, 3)
else:
    print(f"{operator} is not a valid operator")