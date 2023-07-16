def longest(my_list):
    """
    The function takes a list consisting of strings
     and returns the longest string.
    :param my_list: the list object
    :type my_list: list
    :return: the longest string in the list
    :rtype: string
    """
    longest_object = max(my_list, key=len)
    return longest_object


# Course solution:

# def longest(my_list):
#     """Finds the longest string in a list of strings.
#     :param my_list: list of strings
#     :type my_list: list
#     :return: the longest string in my_list
#     :rtype: String
# 	"""
#
#     return max(my_list, key=len)
