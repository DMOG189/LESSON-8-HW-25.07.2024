# LESSON 8 HOMEWORK EX 3

# START

def zugi_print_str(numbers: list[int]) -> str:
    """
    Returns a string indicating whether each number in the list is 'even' or 'odd'.
    """
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(f"{number}: even")
        else:
            result.append(f"{number}: odd")
    return ", ".join(result)

# END