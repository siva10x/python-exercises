# Hello Eagles! 🦅
# Day 13/50 - AI Python Challenge
# List Maximum : Find the largest number in a list without using max() function.
# Use filename as ListMaximum.py
# Our Goal : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI 🔥

def find_maximum(numbers):
    """
    Finds the maximum number in a list without using the max() function.
    
    Args:
    numbers (list): A list of numbers.
    
    Returns:
    int/float: The largest number in the list.
    """
    if not numbers:
        return None  # Return None if the list is empty
    
    maximum = numbers[0]
    
    for number in numbers:
        if number > maximum:
            maximum = number
            
    return maximum

if __name__ == "__main__":
    numbers = input("Enter a list of numbers separated by spaces: ")
    numbers_list = list(map(float, numbers.split()))
    
    max_number = find_maximum(numbers_list)
    
    if max_number is not None:
        print(f"The largest number in the list is: {max_number}")
    else:
        print("The list is empty.")
        
# Sample Output:
# Enter a list of numbers separated by spaces: 3 5 1 8 2
# The largest number in the list is: 8.0
