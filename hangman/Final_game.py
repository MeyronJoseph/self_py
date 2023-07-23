#


picture_1 = """
    x-------x
"""

picture_2 = """
    x-------x
    |
    |
    |
    |
    |
"""

picture_3 = """
    x-------x
    |       |
    |       0
    |
    |
    |
"""

picture_4 = """
    x-------x
    |       |
    |       0
    |       |
    |
    |
"""

picture_5 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
"""

picture_6 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
"""

picture_7 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""


HANGMAN_PHOTOS = {0: picture_1, 1: picture_2, 2: picture_3,
                  3: picture_4, 4: picture_5, 5: picture_6,
                  6: picture_7}


def hangman_opening():
    """

    :return:
    """
    HANGMAN_ASCII_ART = """
    Welcome to the game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                          __/ |                      
                         |___/
    """

    MAX_TRIES = 6

    print(HANGMAN_ASCII_ART, MAX_TRIES)


def print_hangman(num_of_tries):
    """
    Prints the current photo of the hangman depending on the
    number of try.
    :param num_of_tries: int
    :return: the picture of the hangman in this try
    :rtype: str
    """
    current_hangman = HANGMAN_PHOTOS[num_of_tries]
    print(current_hangman)


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


def choose_word(file_path, index):
    """

    :param file_path:
    :param index:
    :return:
    """
    with open(file_path) as file:
        open_word_file = file.read()
    word_list = open_word_file.split()
    word_list_len = len(set(word_list))
    chosen_word = word_list[(index - 1) % len(word_list)]

    return chosen_word


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

num_of_tries = 0
def checking(secret_word, letter_guess, old_letters_guessed):
    """

    :param secret_word:
    :param letter_guess:
    :return:
    """
    global num_of_tries
    if num_of_tries == 6:
        print("LOSE")
        exit()
    if try_update_letter_guessed(letter_guess, old_letters_guessed):
        if letter_guess not in secret_word:
            print(":(")
            num_of_tries += 1
            print_hangman(num_of_tries)
            if num_of_tries == 6:
                print("LOSE")
                exit()
            print(show_hidden_word(secret_word, old_letters_guessed))
        elif letter_guess in secret_word:
            print(show_hidden_word(secret_word, old_letters_guessed))


def main():
    """

    :return:
    """
    hangman_opening()

    user_file_path = input("Please type a file path: ")
    user_word_index = int(input("Please type a number: "))

    secret_word = choose_word(user_file_path, user_word_index)
    old_letters_guessed = []
    user_state = check_win(secret_word, old_letters_guessed)

    print_hangman(num_of_tries)
    print(show_hidden_word(secret_word, old_letters_guessed))

    while user_state is False:
        letter_guess = input("Guess a letter: ")

        checking(secret_word, letter_guess, old_letters_guessed)

        # if num_of_tries == 6:
        #     print("LOSE")
        #     user_state = True
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            user_state = True


if __name__ == "__main__":
    main()