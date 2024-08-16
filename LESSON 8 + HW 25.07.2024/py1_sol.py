# LESSON 8 HOMEWORK EX 1




# START

# py1_sol.py

import py_return_without_func as rwf

# Exercise a: Call ascending_my with 7 and 12
rwf.ascending_my(7, 12)

# Exercise b: Call details_my with "AI is the best"
rwf.details_my("AI is the best")

# Exercise c: Call bool_say with True and False
rwf.bool_say(True)
rwf.bool_say(False)

# Exercise d: Call zugi_print with the list [14, 15, 10, 2, 3, 5]
rwf.zugi_print([14, 15, 10, 2, 3, 5])

# Exercise e: Collect grades from the user, ignoring invalid ones, then call statistics_my
grades = []

while True:
    grade_input = input("Enter a grade (-99 to finish): ")

    try:
        grade = int(grade_input)
        if grade == -99:
            break
        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input, please enter a numeric grade.")

rwf.statistics_my(grades)

# Exercise f: Print help for each function
help(rwf.ascending_my)
help(rwf.details_my)
help(rwf.bool_say)
help(rwf.zugi_print)
help(rwf.statistics_my)

# END