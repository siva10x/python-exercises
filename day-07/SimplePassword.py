# Hello Eagles! 🦅
# *Day 7/50 - AI Python Challenge*
# *Simple Password* : Check if a password meets basic requirements (minimum length).
# Use filename as *SimplePassword.py*
# *Our Goal* : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI ✨

def is_password_valid(password):
    """
    Check if the password meets the minimum length requirement.
    
    Args:
    password (str): The password to check.
    
    Returns:
    str: A message indicating whether the password is valid or not.
    """
    min_length = 8
    if len(password) >= min_length:
        return "Password is valid."
    else:
        return f"Password must be at least {min_length} characters long."
    
# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = is_password_valid(user_password)
    print(result)

# Sample Input/Output
# Enter your password: mypassword
# Password is valid.
# Enter your password: pass
# Password must be at least 8 characters long.
