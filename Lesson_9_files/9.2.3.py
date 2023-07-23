def who_is_missing(file_name):
    """

    :param file_name:
    :return:
    """
    with open(file_name) as file:
        opened_file = file.read()
    file_list = opened_file.split(",")
    sorted_list = sorted(file_list)
    int_list = []
    for num in sorted_list:
        num = int(num)
        int_list.append(num)
    int_list = sorted(int_list)

    missing_number = 0
    int_list_len = len(int_list)
    if int_list[0] != 1:
        missing_number += 1

    for i in range(1, int_list_len):
        if int_list[i] != i+1:
            missing_number += i + 1
            break

    with open("found.txt", "w") as file:
        file.write(str(missing_number))
    return missing_number


# Course solution:


# """Finds a missing number in a sequence of numbers (un-sorted),
# read from a given file.
# Writes the missing number to a new file.
# :param: file_name: path of the file contains th numbers
# :type: string
# :return: n: the missing number
# :rtype: int
# """
# def who_is_missing(file_name):
#     fid = open(file_name, "r")
#     line = fid.read()
#     n_list = [int(n) for n in line.split(',')]
#     fid.close()
#     for n in range(1, len(n_list) + 2):
#         if n not in n_list:
#             fout = open("found.txt", "w")
#             fout.write(str(n))
#             return n
