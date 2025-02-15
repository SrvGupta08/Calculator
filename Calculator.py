# Calculator project

from art import logo

print(logo)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations_symbol = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    continue_calculation = True
    number1 = float(input("What's the first number?: "))

    while continue_calculation:
        for symbol in operations_symbol:
            print(symbol)
        operation = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        answer = operations_symbol[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ").lower()

        if choice == 'y':
            number1 = answer
        else:
            continue_calculation = False
            print("\n" * 50)
            calculator()

calculator()