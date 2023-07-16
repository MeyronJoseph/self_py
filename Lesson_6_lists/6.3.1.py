def are_lists_equal(list1, list2):
    """
    The function accepts only two lists containing elements of the int and float types.
     Returns true if both lists contain exactly the same elements (albeit
     in different order),
     otherwise, the function returns false.
    :param list1: first list
    :param list2: second list
    :type list1: list
    :type list2: list
    :return: Returns true if both lists contain exactly the same elements
    :rtype: boolean
    """
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    if sorted_list1 == sorted_list2:
        return True
    else:
        return False


# Course solution:

# def are_lists_equal(list1,list2):
#     """ Checks if two lists containing ints and floats are equal.
#     :param list1: first list
#     :param list2: second list
#     :type list1: list
#     :type list2: list
#     :return: True if equal, False if not
#     :rtype: boolean
#     """
#     list1.sort()
#     list2.sort()
#     return list1 == list2
