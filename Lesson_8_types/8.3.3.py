def count_chars(my_str):
    """
    Counts the frequency of each char in the input list and builds a
    dictionary, contains the char and its freq.
    :param my_str:
    :type my_str: string
    :return: a dictionary, in the forman [chat, freq]
    :rtype: dict
    """
    str_no_spaces = my_str.replace(" ", "")
    my_dict = {}
    for char in str_no_spaces:
        if char in my_dict.keys():
            continue
        else:
            char_count = str_no_spaces.count(char)
            my_dict[char] = char_count
    return my_dict


ma = "abra cadabra"
print(count_chars(ma))


# Course solution:


# def count_chars(my_str):
#     """Counts the frequency of each char in the input list and builds a
#     dictionary, contains the char and its freq.
#     :param: my_str: the input list of characters
#     :type: list
#     :return: a dictionary, in the forman [chat, freq]
#     :rtype: dictionary
#     """
#
#     my_dict = {}
#     for c in my_str:
#         if c != ' ':
#             if c in my_dict:
#                 my_dict[c] = my_dict[c] + 1
#             else:
#                 my_dict[c] = 1
#     return my_dict
