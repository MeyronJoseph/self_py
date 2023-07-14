# Checking if the last char of the string , is
# showing more than one time in the string.


def last_early(my_str):
    lower_str = my_str.lower()
    last_char = my_str[-1]
    if lower_str.count(last_char) > 1:
        return True
    return False


# Course solution:

# def last_early(my_str):
#     x = my_str.upper()
#     return x[-1] in x[:-1]
