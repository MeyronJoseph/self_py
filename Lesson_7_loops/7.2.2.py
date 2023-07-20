def numbers_letters_count(my_str):
    """
    The function takes as a string parameter.
    Returns a list where the first member represents the number
    of digits in the string,
    and the second member represents the number of
    letters in the string, including spaces, periods,
    punctuation, and anything other than digits.
    :param my_str: the object to work on
    :type my_str: string
    :return: Returns a list where the first member represents the number of digits in the string,
    and the second member
    represents the number of letters in the string
    including spaces, periods, punctuation,
    and anything other than digits.
    :rtype: list
    """
    count_numbers = 0
    count_chars = 0
    for char in my_str:
        if char.isdigit():
            count_numbers += 1
        else:
            count_chars += 1
    numbers_letters_list = [count_numbers, count_chars]
    return numbers_letters_list


# Course solution:


# def numbers_letters_count(my_str):
#     """Counts number of digits and non-digits in "my_str".
#     :param my_str: input string, contains characters
#     :type my_str: string
#     :return: 2-element list: the first element is the number of digits in my_str
#     the second one is the number of non-digit characters in my_str
#     :rtype: list.
# 	"""
#
#     digits = [char for char in my_str if char >= '0' and char <= '9']
#     return [len(digits), len(my_str)-len(digits)]
