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


HANGMAN_PHOTOS = {1: picture_1, 2: picture_2, 3: picture_3,
                  4: picture_4, 5: picture_5, 6: picture_6,
                  7: picture_7}


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
