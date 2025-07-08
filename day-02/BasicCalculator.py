# Hello Eagles! 🦅
# *Day 2/50 - AI Python Challenge*
# *Basic Calculator* : Simple calculator for two numbers with +, -, *, / operations.
# Use filename as *BasicCalculator.py*
# *Our Goal* : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI ✨

# Function to perform basic arithmetic operations
def basic_calculator(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."
    
# Main function to execute the script
def main():
    # Input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Input the operation
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the calculation
    result = basic_calculator(num1, num2, operation)
    
    # Display the result
    print(f"The result of {num1} {operation} {num2} is: {result}")

# Execute the main function
if __name__ == "__main__":
    main()

# Sample Input/Output
# Enter the first number: 10
# Enter the second number: 5
# Enter the operation (+, -, *, /): +
# The result of 10.0 + 5.0 is: 15.0