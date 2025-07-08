# Hello Eagles! 🦅
# *Day 1/50 - AI Python Challenge*
# *Personal Greeting* : Ask for name, age, and favorite color, then create a personalized message.
# Use filename as *PersonalGreeting.py*
# *Our Goal* : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI ✨

# Function to create a personalized greeting message
def create_greeting(name, age, favorite_color):
    return f"Hello {name}! You are {age} years old and your favorite color is {favorite_color}. Have a great day!"

# Main function to execute the script
def main():
    # Ask for user's name, age, and favorite color
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    favorite_color = input("Enter your favorite color: ")
    
    # Create the personalized greeting message
    greeting_message = create_greeting(name, age, favorite_color)
    
    # Display the greeting message
    print(greeting_message)

# Execute the main function
if __name__ == "__main__":
    main()

# Sample Input/Output
# Enter your name: John
# Enter your age: 25
# Enter your favorite color: Blue
# Hello John! You are 25 years old and your favorite color is Blue. Have a great day!
