def are_files_equal(file1, file2):
    """
    Comparing 2 files.
    :param file1: first file to compare
    :param file2: second file to compare
    :type file1: string
    :type file2: str
    :return: True if equal, False otherwise
    :rtype: boolean
    """
    open_file1 = open(file1, "r")
    file_1_text = open_file1.read()

    open_file2 = open(file2, "r")
    file_2_text = open_file2.read()

    if file_1_text == file_2_text:
        return True
    else:
        return False


# Course solution:


# """Compares 2 files.
#     :param: file1, file2: path of compared files
#     :type: string
#     :return: True if files equal, False if not
#     :rtype: boolean
# """
# def are_files_equal(file1, file2):
# 	with open(file1,'r') as input_file1, \
# 	     open(file2,'r') as input_file2:
# 			rawData1=input_file1.read()
# 			rawData2=input_file2.read()
# 			if (rawData1==rawData2):
# 				return True
# 			else:
# 				return False
