# Hello Eagles! 🦅
# *Day 6/50 - AI Python Challenge*
# *Number Comparison* : Compare two numbers and tell which is larger, smaller, or if they're equal.
# Use filename as *NumberComparison.py*
# *Our Goal* : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI ✨

def compare_numbers(num1, num2):
    if num1 > num2:
        return f"{num1} is larger than {num2}."
    elif num1 < num2:
        return f"{num1} is smaller than {num2}."
    else:
        return f"{num1} is equal to {num2}."
    
# Example usage
if __name__ == "__main__":
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        result = compare_numbers(number1, number2)
        print(result)
    except ValueError:
        print("Please enter valid numbers.")

# Sample Input/Output
# Enter the first number: 10
# Enter the second number: 5
# 10.0 is larger than 5.0.
