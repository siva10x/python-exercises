# Hello Eagles! 🦅
# Day 12/50 - AI Python Challenge
# Countdown Timer : Create a simple countdown from 10 to 0.
# Use filename as CountdownTimer.py
# Our Goal : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI 🔥

import time
def countdown_timer(start=10):
    while start >= 0:
        print(start)
        time.sleep(1)  # Wait for 1 second
        start -= 1
    print("Countdown finished!")

if __name__ == "__main__":
    # input from user
    start_number = int(input("Enter the starting number for countdown: "))
    countdown_timer(start_number)
# You can change the starting number by passing an argument to countdown_timer
# For example: countdown_timer(5) will count down from 5 to 0

# Sample Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# Countdown finished!