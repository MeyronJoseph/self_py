#


user_string = input("Please enter a string: ")
string_length = len(user_string)
divided_length = string_length // 2
string_first_half = user_string[:divided_length].lower()
string_last_half = user_string[divided_length:].upper()
new_string = string_first_half + string_last_half
print(new_string)


# Course solution:
# fix_me = input("enter string:")
# half = round(len(fix_me)/2)
# print(fix_me[:half].lower() + fix_me[half:].upper())
