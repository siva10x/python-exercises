# Hello Eagles! 🦅
# Day 11/50 - AI Python Challenge
# Grade Average : Calculate average of 5 test scores and determine pass/fail.
# Use filename as GradeAverage.py
# Our Goal : Use any AI tool to generate the script and execute the script without issue
# This is automated AI Message
# #FlyHighwithAI 🔥

def calculate_average(grades):
    return sum(grades) / len(grades)

def determine_pass_fail(average):
    if average >= 60:
        return "Pass"
    else:
        return "Fail"
    
if __name__ == "__main__":
    grades = []
    for i in range(5):
        score = float(input(f"Enter score for test {i + 1}: "))
        grades.append(score)
    
    average = calculate_average(grades)
    result = determine_pass_fail(average)
    
    print(f"Average score: {average:.2f}")
    print(f"Result: {result}")
    
# Sample Output:
# Enter score for test 1: 85
# Enter score for test 2: 90
# Enter score for test 3: 78
# Enter score for test 4: 88
# Enter score for test 5: 92
# Average score: 86.60
# Result: Pass

