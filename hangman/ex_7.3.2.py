def check_win(secret_word, old_letters_guessed):
    """
    Checks if the player succeeded to guess the whole secret word.
    :param secret_word: The word to be guessed by the player
    :param old_letters_guessed: Previous guessed letters
    :type secret_word: string
    :type old_letters_guessed: list
    :return: True if the player succeeded and False otherwise
    :rtype: boolean
    """
    if len(secret_word) == 0:
        return True
    for char in secret_word:
        if char not in old_letters_guessed:
            return False
    return True


# Course solution:


# def check_win(secret_word, old_letters_guessed):
#     """Checks if the whole secret word was guessed correctly
#    	:param: secret_word: the word to be guessed
#     :param: old_letters_guessed: the letters that were guessed (user's input)
#     :type secret_word: list
#     :type old_letters_guessed: list
#     :return: True if the secret word was guessed, False if not
#     :rtype: boolean
#     """
#     for letter in secret_word:
#         if letter not in old_letters_guessed:
#             return False
#     return True
