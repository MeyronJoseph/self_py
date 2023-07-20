def key_l(tuples):
    return tuples[1]


def sort_prices(list_of_tuples):
    sorted_tuple_list = sorted(list_of_tuples, key=key_l, reverse=True)
    return sorted_tuple_list


# Course solution:


# def sort_prices(list_of_tuples):
#     """Sorts items according to their price, from higher to lower.
#     :param: list_of_tuples: the input list, each tuple contains an item and its
#     price
#     :param: list of tuples. price is double
#     :return: sorted list
#     :rtype: list of tuples.
#     """
#
#     list_of_tuples.sort(key=lambda x: x[1])
#     list_of_tuples.reverse()
#     return list_of_tuples
