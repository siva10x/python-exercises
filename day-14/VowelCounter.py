# Hello Eagles! 🦅
# Day 14/50 - AI Python Challenge
# Vowel Counter : Count how many vowels are in a given word.
# Use filename as VowelCounter.py
# Our Goal : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI 🔥

def count_vowels(word):
    """
    Counts the number of vowels in a given word.
    
    Args:
    word (str): The word to count vowels in.
    
    Returns:
    int: The number of vowels in the word.
    """
    vowels = "aeiouAEIOU"
    count = sum(1 for char in word if char in vowels)
    return count

if __name__ == "__main__":
    word = input("Enter a word: ")
    vowel_count = count_vowels(word)
    print(f"The number of vowels in '{word}' is: {vowel_count}")

# Sample Output:
# Enter a word: Hello
# The number of vowels in 'Hello' is: 2
