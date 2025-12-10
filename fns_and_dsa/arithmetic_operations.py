# Arithmetic Operations Function
# This module defines a function that performs basic arithmetic operations

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.
    
    Parameters:
    num1 (float): The first number
    num2 (float): The second number
    operation (string): The operation to perform ('add', 'subtract', 'multiply', or 'divide')
    
    Returns:
    The result of the arithmetic operation, or an error message for division by zero
    """
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Error: Invalid operation. Use 'add', 'subtract', 'multiply', or 'divide'."
