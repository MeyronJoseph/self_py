import itertools


def extend_list_x(list_x, list_y):
    """
    The function takes two list_y lists, list_x.
     The function expands the list_x (modifies it) to include the list_y at the beginning,
     and returns the list_x.
    :param list_x: first list
    :param list_y: second list
    :type list_x: list
    :type list_y: list
    :return: list_x with list_y in the beginning
    :rtype: list
    """

    list_x = list(itertools.chain(list_y, list_x))
    return list_x


# Course solution:

# def extend_list_x(list_x, list_y):
#     """Gets two lists, appends the second one at the beginning of the first one.
#     :param list_x: first list
#     :param list_y: second list
#     :type list_x: list
#     :type list_y: list
#     :return: the appended list: [list_y list_x]
#     :rtype: list
# 	"""
#
#     list_x[:0] = list_y
#     return list_x
