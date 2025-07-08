# Hello Eagles! 🦅
# *Day 4/50 - AI Python Challenge*
# *Age Category* : Determine if someone is a child, teenager, adult, or senior based on age.
# Use filename as *AgeCategory.py*
# *Our Goal* : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI ✨

# Function to determine age category
def determine_age_category(age):
    if age < 0:
        return "Error: Age cannot be negative."
    elif age <= 12:
        return "You are a child."
    elif age <= 19:
        return "You are a teenager."
    elif age <= 64:
        return "You are an adult."
    else:
        return "You are a senior."
    
# Main function to execute the script
def main():
    try:
        # Input age from user
        age = int(input("Enter your age: "))
        
        # Determine the age category
        category = determine_age_category(age)
        
        # Display the result
        print(category)
    
    except ValueError:
        print("Please enter a valid integer for age.")

# Execute the main function
if __name__ == "__main__":
    main()