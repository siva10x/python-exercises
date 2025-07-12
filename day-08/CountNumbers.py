# Hello Eagles! 🦅
# Day 8/50 - AI Python Challenge
# Count Numbers : Count how many positive, negative, and zero numbers are in a list.
# Use filename as CountNumbers.py
# Our Goal : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI 🔥

def count_numbers(numbers):
    """
    Count how many positive, negative, and zero numbers are in a list.
    
    Args:
    numbers (list): A list of integers.
    
    Returns:
    tuple: A tuple containing counts of positive, negative, and zero numbers.
    """
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for number in numbers:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1
            
    return positive_count, negative_count, zero_count

# Example usage
if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]
    # Now you can use numbers as your list
    pos_count, neg_count, zero_count = count_numbers(numbers)
    print(f"Positive numbers: {pos_count}")
    print(f"Negative numbers: {neg_count}")
    print(f"Zero numbers: {zero_count}")

# Sample Input/Output
# Enter numbers separated by spaces: 1 -2 0 3 -4 0
# Positive numbers: 2
# Negative numbers: 2
# Zero numbers: 2
# Enter numbers separated by spaces: -1 -2 -3
# Positive numbers: 0
# Negative numbers: 3
# Zero numbers: 0
