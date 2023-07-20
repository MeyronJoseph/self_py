def seven_boom(end_number):
    """
    append all numbers in range to a list, except numbers that contains the number 7,
    or is divided by 7, then it appends the string "BOOM".
    :param end_number: the last number of the range
    :type end_number: int
    :return: list that contains numbers in a row and "BOOM" instead
    of the numbers that are divided by 7 or contains the digit 7.
    :rtype: list
    """
    boom_list = []
    for num in range(end_number + 1):
        if num % 7 == 0 or "7" in str(num):
            boom_list.append("BOOM")
        else:
            boom_list.append(num)
    return boom_list


# Course solution:

# def boomify(num):
#     """Checks if a num is a multiple of 7 or contains 7. Returns 'BOOM' if TRUE,
#     num otherwise.
#     :param num: the number to be checked
#     :type num: int
#     returns 'BOOM' or num
#     rtype: int or str
#     """
#     if num % 7 == 0 or '7' in str(num):
#         return 'BOOM'
#     else:
#         return num
#
#
# def seven_boom(end_number):
#     """Implements 7-BOOM game: gets a number as an input, returns a list in the
#     range of 0-number in which all numbers that are multiples of 7 or contains â€˜7â€™
#     are replaced by â€œBOOMâ€.
#    	:param end_number: input number
#    	:type end_number: int
#    	returns the list of numbers 0-end_number, with the correct changes
#    	:rtype: list
# 	"""
#
#     return [boomify(i) for i in range(end_number + 1)]
