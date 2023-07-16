def is_valid_input(letter_guessed):
    """
    Checking if player guess contains 1 char that is
    in the abc.
    :param letter_guessed: player guess
    :type letter_guessed: str
    :return: If the char is valid or not
    :rtype: True / False, bool type
    """

    len_player_input = len(letter_guessed)

    if len_player_input >= 2 or letter_guessed.isalpha() is False:
        return False
    else:
        return True




#################################
# Course solution:

# def is_valid_input(letter_guessed):
#     """Checks the validation of input (character)
#     :param: letter_guessed: user guess
#     :type: string
#     :return: Whether or not the input was valid
#     :rtype: boolean
#     """
#     char = letter_guessed
#     if len(char) == 1 and char.isalpha():
#         return True
#     else:
#         return False
