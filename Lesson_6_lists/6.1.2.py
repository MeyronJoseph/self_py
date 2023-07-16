def shift_left(my_list):
    """
    getting a list with 3 items, and move every item 1 to the left
    :param my_list:
    :type my_list: list
    :return: new list with every item 1 movement to the left
    :rtype: list
    """

    # Changing every index 1 to the left to create the new list
    my_list[-1], my_list[0], my_list[1] = my_list[0], my_list[1], my_list[2]
    return my_list



# Course solition:

# def shift_left(my_list):
#     """Gets a list with 3 elements, returns the same list but left-shifted.
#     :param my_list: a list with 3 elements.
#     :type my_list: list
#     :return: the same list, left shifted.
#     :rtype: list.
# 	"""
#
#     new_list = [my_list[1], my_list[2], my_list[0]]
#     return new_list