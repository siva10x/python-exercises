# Hello Eagles! 🦅
# Day 9/50 - AI Python Challenge
# Sum Calculator : Find sum of all numbers from 1 to n using a loop.
# Use filename as SumCalculator.py
# Our Goal : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI 🔥

# calculate sum using a loop
def calculate_sum(n):
    """
    Calculate the sum of all numbers from 1 to n using a loop.
    
    Args:
    n (int): The upper limit for the sum.
    
    Returns:
    int: The sum of all numbers from 1 to n.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total 

# calculate sum using a formula
def calculate_sum_formula(n):
    """
    Calculate the sum of all numbers from 1 to n using the formula n(n + 1) / 2.
    
    Args:
    n (int): The upper limit for the sum.
    
    Returns:
    int: The sum of all numbers from 1 to n.
    """
    return n * (n + 1) // 2

# Example usage
if __name__ == "__main__":
    try:
        user_input = int(input("Enter a positive integer n: "))
        if user_input < 1:
            print("Please enter a positive integer greater than 0.")
        else:
            result_loop = calculate_sum(user_input)
            print(f"Loops: The sum of all numbers from 1 to {user_input} is: {result_loop}")
            result_formula = calculate_sum_formula(user_input)
            print(f"Formula: The sum of all numbers from 1 to {user_input} is: {result_formula}")
    except ValueError:
        print("Invalid input! Please enter a valid positive integer.")

# Sample Input/Output
# Enter a positive integer n: 5
# Loops: The sum of all numbers from 1 to 5 is: 15
# Formula: The sum of all numbers from 1 to 5 is: 15
# Enter a positive integer n: 10
# Loops: The sum of all numbers from 1 to 10 is: 55
# Formula: The sum of all numbers from 1 to 10 is: 55 
# Enter a positive integer n: -3
# Please enter a positive integer greater than 0.
# Enter a positive integer n: abc
# Invalid input! Please enter a valid positive integer.