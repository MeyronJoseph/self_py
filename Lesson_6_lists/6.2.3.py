def format_list(my_list):
    """
    Making a string containing the list members in the even
    positions, separated by a comma and space, plus the
    last member with the inscription "and" before it.
    :param my_list: list with even len
    :type my_list: list
    :return: string containing the list members with the even positions,
    separated by a comma and the word "and"
    :rtype: string
    """
    new_list = ", ".join(my_list[0:-1:2]) + ", and " + str(my_list[-1])
    return new_list


# Course solution:

# def format_list(my_list):
#     """Chains all even elements of a list-of-strings into one string.
#     Elements in the list are separated by ",". The last element will be added
#     after the even element, with "and" between them.
#     :param my_list: an even-length list of strings.
#     :type my_list: list
#     :return: the new chained string.
#     :rtype: string.
# 	"""
#
#     result = ', '.join(my_list[:-1:2])
#     result = result + ', and ' + my_list[-1]
#     return result