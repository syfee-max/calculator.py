# calculator.py
# A simple command-line calculator
# Created by syafi faisal

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def calculator():
    print("Simple Calculator")
    print("------------------")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter operation (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == '1':
        result = add(num1, num2)
        operator = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operator = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operator = '*'
    elif choice == '4':
        result = divide(num1, num2)
        operator = '/'

    print(f"Result: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()
