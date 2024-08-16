# LESSON 8 HOMEWORK EX 5

# START


def int_get(prompt: str) -> int:
    """
    Repeatedly prompts the user for an integer input using the provided prompt.
    If the user enters a non-integer value, the function will catch the exception and prompt again.
    Returns the valid integer input.
    """
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

# END