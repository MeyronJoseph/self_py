#


def filter_teens(a=13, b=13, c=13):
    a = fix_age(a)
    b = fix_age(b)
    c = fix_age(c)
    sum_ages = a + b + c
    return sum_ages


def fix_age(age):
    if 13 <= age <= 19 and age not in [15, 16]:
        age = 0
    return age


print(filter_teens())
print(filter_teens(1, 2, 3))
print(filter_teens(2, 13, 1))
print(filter_teens(2, 1, 15))


# Course solution:

# def filter_teens(a=13, b=13, c=13):
#     return fix_teen(a) + fix_teen(b) + fix_teen(c)
#
#
# def fix_teen(n):
#     if n in (13, 14, 17, 18, 19):
#         return 0
#     return n