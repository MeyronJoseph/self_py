#


is_palindrom = input("Enter a word: ")
pal_no_space = is_palindrom.replace(" ", "")
pal_lower = pal_no_space.lower()
un_reversed_pal = pal_lower
reversed_pal = un_reversed_pal[::-1]

if un_reversed_pal == reversed_pal:
    print("OK")
else:
    print("NOT")


# Course solution:
# source = input("Enter a word: ").replace(' ', '').lower()
# if source == source[::-1]:
#     print('OK')
# else:
#     print('NOT')

