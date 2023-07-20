def sort_anagrams(list_of_strings):
    """
    Splits a list of words into sub-lists, each contains anagrams of words from
    the original list.
    :param: list_of_strings: the given list of words
    :type: list of lists
    :return: list of anagram-lists
    :rtype: list of lists
    """
    updated_list = []
    for string in list_of_strings:
        found = False
        for sublist in updated_list:
            if sorted(sublist[0]) == sorted(string):
                sublist.append(string)
                found = True
                break
        if not found:
            updated_list.append([string])
    return updated_list


# Another code I found that works:


# def sort_anagrams(list_of_strings):
#     """This function does something with list"""
#     sorted_list_of_string = list()
#     returned_list_of_strings = list()
#     elements_bank = list()
#     for element in list_of_strings:
#         sorted_element = ''.join(sorted(element))
#     for element in sorted_list_of_string:
#         if element not in elements_bank:
#             element_list = list()
#             for i in range(len(sorted_list_of_string)):
#                 if sorted_list_of_string[i] == element:
#                     element_list.append(list_of_strings[i])
#                     elements_bank.append(element)
#             returned_list_of_strings.append(element_list)
#         else:
#             continue
#     return returned_list_of_strings
#         sorted_list_of_string.append(sorted_element)


def main():
    list_of_words = [
        'deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating',
        'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening',
        'lasted', 'resmelts'
    ]
    print(sort_anagrams(list_of_words))


if __name__ == '__main__':
    main()


# Course solution:


# def sort_anagrams(list_of_strings):
#     """Splits a list of words into sub-lists, each contains anagrams of words from
#     the original list.
#     :param: list_of_strings: the given list of words
#     :type: list of lists
#     :return: list of anagram-lists
#     :rtype: list of lists
#     """
#
#     result = []
#     for string in list_of_strings:
#         if set(string) in [set(s[0]) for s in result]:
#             for s in result:
#                 if set(string) == set(s[0]):
#                     s.append(string)
#         else:
#             result.append([string])
#     return result
