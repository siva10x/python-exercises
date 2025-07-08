# Hello Eagles! 🦅
# *Day 3/50 - AI Python Challenge*
# *Even or Odd Checker* : Check if a number is even or odd, then check a list of numbers.
# Use filename as *EvenOddChecker.py*
# *Our Goal* : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI ✨

# Function to check if a number is even or odd
def is_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."
    
# Main function to execute the script
def main():
    # Input a number to check
    try:
        number = int(input("Enter a number to check if it's even or odd: "))
        result = is_even_or_odd(number)
        print(result)
        
        # Input a list of numbers to check
        numbers_list = input("Enter a list of numbers separated by spaces: ")
        numbers = map(int, numbers_list.split())
        
        # Check each number in the list
        for num in numbers:
            print(is_even_or_odd(num))
    
    except ValueError:
        print("Please enter valid integers.")

# Execute the main function
if __name__ == "__main__":
    main()

# Sample Input/Output
# Enter a number to check if it's even or odd: 4
# 4 is even.

# Enter a list of numbers separated by spaces: 1 2 3 4
# 1 is odd.
# 2 is even.
# 3 is odd.
# 4 is even.
