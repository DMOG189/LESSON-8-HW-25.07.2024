# LESSON 8 HOMEWORK EX 4

# START


def zugi_list_str(numbers: list[int]) -> list[str]:
    """
    Returns a list of strings indicating whether each number in the list is 'even' or 'odd'.
    """
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(f"{number}: even")
        else:
            result.append(f"{number}: odd")
    return result

# END