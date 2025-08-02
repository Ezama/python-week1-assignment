# Introduction
print("Welcome to the Python Calculator Program!")
print("Instructions: Enter two numbers and choose an operation to perform.")

# variable initialization
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation based on the chosen operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Check for division by zero
    if num2 == 0:
        result = "Error: Cannot divide by zero!"
    else:
        result = num1 / num2
# In case of an invalid operation
else:
    result = "Invalid operation"

# Display the result
print("Result:", result)
