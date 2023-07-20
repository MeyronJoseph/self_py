def is_greater(my_list, n):
    """
    The function takes two parameters: list and number n.
    Returns a new list of all elements greater than n.
    :param my_list: list with numbers
    :param n: a number
    :type my_list: list
    :type n: int
    :return: Returns a new list of all
    elements greater than n.
    :rtype: list
    """
    new_list = []
    for num in my_list:
        if num > n:
            new_list.append(num)
    return new_list



# Course solution:


# def is_greater(my_list, n):
#     """Returns all the numbers in "my_list" which are bigger than "n".
#     :param my_list: a list of numbers.
#     :param n: the number to which "my_list" numbers are compared.
#     :type my_list: list
#     :type n: float
#     :return: list of numbers of â€œmy_listâ€ which are bigger than "n".
#     :rtype: list.
# 	"""
#
#     return [l for l in my_list if l > n]
