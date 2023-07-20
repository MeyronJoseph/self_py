def sequence_del(my_str):
    """
    The function takes a string and deletes the letters that appear in the sequence.
    That is, the function returns a string in which only one character appears
    from each sequence of identical characters in the input string.
    :param my_str: the input str
    :type my_str: string
    :return: a string in which only one character appears
    from each sequence of identical characters in the input string.
    :rtype: list
    """
    if len(my_str) == 0:
        return my_str
    new_string = my_str[0]
    for char in my_str:
        if char == new_string[-1]:
            continue
        else:
            new_string = new_string + char
    return new_string


# Course solution:


# def sequence_del(my_str):
#     """Deletes all letter duplicates in the input string.
#     :param my_str: input string
#     :type my_str: string.
#     :return: the input string, without duplicates (one letter out of each sequence)
#     :rtype: string.
# 	"""
#     if len(my_str) > 0:
#         result = my_str[0]
#         for char in my_str[1:]:
#             if char != result[-1]:
#                 result = result + char
#         return result
#     return my_str
