def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

if __name__ == "__main__":
    print("--- GitHub Code Test: Basic Calculator ---")
    
    num1 = 15
    num2 = 5
    
    # Performing calculations
    print(f"Addition:       {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction:    {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    print(f"Division:       {num1} / {num2} = {divide(num1, num2)}")

