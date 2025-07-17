# Hello Eagles! 🦅
# Day 15/50 - AI Python Challenge
# Name Formatter : Take a full name and display it in different formats (Last, First etc.).
# Use filename as NameFormatter.py
# Our Goal : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI 🚀

def format_name(full_name):
    """
    Formats the given full name into different styles.
    
    Args:
    full_name (str): The full name to format.
    
    Returns:
    dict: A dictionary containing the formatted names.
    """
    names = full_name.strip().split()
    
    if len(names) < 2:
        return {"error": "Please provide both first and last names."}
    
    first_name = names[0]
    last_name = names[-1]
    
    return {
        "first_last": f"{first_name} {last_name}",
        "last_first": f"{last_name}, {first_name}",
        "first_initial_last": f"{first_name[0]}. {last_name}",
        "last_initial_first": f"{last_name[0]}. {first_name}"
    }   

if __name__ == "__main__":
    full_name = input("Enter your full name: ")
    formatted_names = format_name(full_name)
    
    if "error" in formatted_names:
        print(formatted_names["error"])
    else:
        print("Formatted Names:")
        for style, name in formatted_names.items():
            print(f"{style.replace('_', ' ').title()}: {name}")

# Sample Output:
# Enter your full name: John Doe
# Formatted Names:
# First Last: John Doe
# Last First: Doe, John
# First Initial Last: J. Doe
# Last Initial First: D. John