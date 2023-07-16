# Upgrading ex_5.5.1 to a better version


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Returns a Boolean value representing the integrity
    of the string and whether the user has
     previously guessed the character.
    :param letter_guessed: player guess input
    :param old_letters_guessed: list of old guessed letters
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True or False if the input is valid
    :rtype: boolean
    """
    guess_len = len(letter_guessed)
    lower_letter_guessed = letter_guessed.lower()
    if guess_len >= 2 or not(letter_guessed.isalpha()) or lower_letter_guessed in old_letters_guessed:
        return False
    if guess_len == 1 and letter_guessed.isalpha() and lower_letter_guessed not in old_letters_guessed:
        return True


# Course solution:

# def check_valid_input(letter_guessed, old_letters_guessed):
#     """Checks the validation of user input, e.g. one English letter, not entered
#     before
#     :param letter_guessed: user input
#     :param old_letters_guessed: previous inputs
#     :type letter_guessed: string
#     :type old_letters_guessed: list
#     :return: True if input is valid, False if not.
#     :rtype: boolean
#     """
#
#     return len(letter_guessed) == 1 and letter_guessed.isalpha() \
#            and not letter_guessed.lower() in old_letters_guessed
