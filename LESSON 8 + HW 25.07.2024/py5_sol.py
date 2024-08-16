# LESSON 8 HOMEWORK EX 5

# START

import py_return_with_func as rwf

# Function to collect grades using int_get
grades = []

while True:
    grade = rwf.int_get("Enter a grade (-99 to finish): ")

    if grade == -99:
        break
    if 0 <= grade <= 100:
        grades.append(grade)
    else:
        print("Grade must be between 0 and 100.")

# Call statistics_my with the collected grades
rwf.statistics_my(grades)

# Print help for the int_get function
help(rwf.int_get)

# END