def show_hidden_word(secret_word, old_letters_guessed):
    """
    The function returns a string consisting of letters and underscores.
    The string shows the letters from the old_letters_guessed list that
    are in the secret_word string in their appropriate position,
    and the other letters in the string
    (which the player has not yet guessed) as underlines.
    :param secret_word: The secret word the player has to guess
    :param old_letters_guessed: Letters that the player has guessed so far
    :type secret_word: string
    :type old_letters_guessed: list
    :return: a string consisting of letters and underscores
    :rtype: string
    """
    player_letters_lines_display = ""
    for char in secret_word:
        if char in old_letters_guessed:
            player_letters_lines_display += char + " "
        else:
            player_letters_lines_display += "_ "
    return player_letters_lines_display[:-1]


# Course solution:


# def show_hidden_word (secret_word, old_letters_guessed):
#     """Displays guessed letters in the secret word, and '_' for letters that were
#     not guessed yet
#     :param: secret_word: the word to be guessed
#     :param: old_letters_guessed: the letters that were guessed (user's input)
#     :type secret_word: list
#     :type old_letters_guessed: list
#     :return: the updated list, with all guessed letters
#     :rtype: list
#     """
#     result = ''
#     for letter in secret_word:
#         if letter in old_letters_guessed:
#             result = result + letter + ' '
#         else:
#             result = result + "_ "
#     return result[:-1]
