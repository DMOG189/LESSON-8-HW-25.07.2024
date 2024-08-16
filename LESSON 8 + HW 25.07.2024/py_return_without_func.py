# LESSON 8 HOMEWORK EX 1



# START

def ascending_my(num1: int, num2: int):
    """
    Prints the two numbers in ascending order.
    """
    if num1 < num2:
        print(num1, num2)
    else:
        print(num2, num1)


def details_my(string: str):
    """
    Prints the first, middle, and last characters of the string.
    """
    length = len(string)
    first_char = string[0]
    last_char = string[-1]
    middle_char = string[length // 2]

    print(f"First character: {first_char}")
    print(f"Middle character: {middle_char}")
    print(f"Last character: {last_char}")


def bool_say(value: bool):
    """
    Prints 'yes' if the boolean is True, otherwise prints 'no'.
    """
    if value:
        print("yes")
    else:
        print("no")


def zugi_print(numbers: list[int]):
    """
    Prints whether each number in the list is 'even' or 'odd'.
    """
    for number in numbers:
        if number % 2 == 0:
            print(f"{number}: even")
        else:
            print(f"{number}: odd")


def statistics_my(grades: list[int]):
    """
    Prints the highest grade, lowest grade, number of grades, average grade,
    number of excellent grades (over 90), number of failing grades (below 55),
    and the standard deviation.
    """
    if not grades:
        print("No grades to display.")
        return

    highest_grade = max(grades)
    lowest_grade = min(grades)
    num_grades = len(grades)
    average_grade = sum(grades) / num_grades
    excellent_grades = len([grade for grade in grades if grade > 90])
    failing_grades = len([grade for grade in grades if grade < 55])
    standard_deviation = (sum((x - average_grade) ** 2 for x in grades) / num_grades) ** 0.5

    print(f"Highest grade: {highest_grade}")
    print(f"Lowest grade: {lowest_grade}")
    print(f"Number of grades: {num_grades}")
    print(f"Average grade: {average_grade:.2f}")
    print(f"Number of excellent grades (over 90): {excellent_grades}")
    print(f"Number of failing grades (below 55): {failing_grades}")
    print(f"Standard deviation: {standard_deviation:.2f}")

# END