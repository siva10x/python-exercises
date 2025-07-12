# Hello Eagles! 🦅
# Day 10/50 - AI Python Challenge
# Name List : Store 5 names in a list and print them with their lengths.
# Use filename as NameList.py
# Our Goal : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI 🔥

def print_name_lengths(names):
    """
    Print each name in the list along with its length.
    
    Args:
    names (list): A list of names.
    """
    for name in names:
        print(f"{name}: {len(name)} characters")

# Example usage
if __name__ == "__main__":
    # Take 5 names as input from the user
    for i in range(5):
        name = input(f"Enter name {i + 1}: ")
        if i == 0:
            name_list = [name]  # Initialize the list with the first name
        else:
            name_list.append(name)  # Append subsequent names

    # Print the names and their lengths
    print()
    print_name_lengths(name_list)

# Sample Input/Output
# Enter name 1: Alice
# Enter name 2: Bob
# Enter name 3: Charlie
# Enter name 4: David
# Enter name 5: Eve
#
# Alice: 5 characters
# Bob: 3 characters
# Charlie: 7 characters
# David: 5 characters
# Eve: 3 characters