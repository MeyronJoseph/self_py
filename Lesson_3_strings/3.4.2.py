# need to add explanation


user_string = input("Please enter a string: ")
first_char_in_string = user_string[0]
string_without_first_char = user_string[1:]
string_replace = string_without_first_char.replace(first_char_in_string, "e")
updated_string = first_char_in_string + string_replace
print(updated_string)


# course solution:
# fix_me = input("Enter a string: ")
# first_letter = fix_me[0]
# print(first_letter + fix_me[1:].replace(first_letter, 'e'))
