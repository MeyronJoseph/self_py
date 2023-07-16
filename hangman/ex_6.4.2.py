# Using 6.4.1 to make a new upgraded function to the input
# of the player valid check and return value


def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks the validation of user input, e.g. one English letter, not entered
    before
    :param letter_guessed: user input
    :param old_letters_guessed: previous inputs
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True if input is valid, False if not.
    :rtype: boolean
    """

    return len(letter_guessed) == 1 and letter_guessed.isalpha() and not letter_guessed.lower() in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    if we get True from the "check_valid_input" function, we append
    the item to the guessed list and return True.
    if we get False, we print X and show the list with " -> "
    between.
    :param letter_guessed: player input
    :param old_letters_guessed: previous inputs
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True or False and actions upon them.
    :rtype: boolean
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        sorted_list = sorted(old_letters_guessed)
        message = " -> ".join(sorted_list).lower()
        print(message)
        return False
