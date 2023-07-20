def squared_numbers(start, stop):
    """
    The function takes two integers.
    Returns a list of all squares of numbers between start and stop (inclusive).
    :param start: first number
    :param stop: last number
    :type start: int
    :type stop: int
    :return: Returns a list of all squares of
    numbers between start and stop (inclusive).
    :rtype: list
    """
    squared_numbers_list = []
    while start <= stop:
        squared_number = start ** 2
        squared_numbers_list.append(squared_number)
        start += 1
    return squared_numbers_list

