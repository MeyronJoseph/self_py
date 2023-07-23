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

    return word_list_len, chosen_word
