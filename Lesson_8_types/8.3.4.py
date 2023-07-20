def inverse_dict(my_dict):
    """
     Each dictionary key that is passed is a dictionary entry that is returned,
     and every dictionary entry that is passed is a key in the dictionary that is returned.
    :param my_dict: The given dict from the user
    :type my_dict: dict
    :return: Returns a new dictionary with "inverse" mapping
    :rtype: dict
    """
    new_dict = {}
    for key, value in my_dict.items():
        if value in new_dict:
            new_dict[value].append(key)
        else:
            new_dict[value] = [key]
    for value in new_dict.values():
        value.sort()
    return new_dict


# Course solution:


# def inverse_dict(my_dict):
#     """cross-changes values and keys in a dictionary: each value becomes a key and
#     each key becomes a value.
#     :param: my_dict: the input dictionary
#     :type: tuple
#     :return: the cross-changed dictionary
#     :rtype: tuple
#     """
#
#     new_dict = {}
#     for key in my_dict:
#         if my_dict[key] in new_dict:
#             new_dict[my_dict[key]].append(key)
#         else:
#             new_dict[my_dict[key]] = [key]
#     for key in new_dict:
#         new_dict[key].sort()
#     return new_dict
