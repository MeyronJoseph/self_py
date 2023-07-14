#


def chocolate_maker(small, big, x):
    total_small = small * 1
    total_big = big * 5
    if x - total_big == 0:
        return True
    if x - total_big > 0:
        if total_small >= x:
            return True
        else:
            return False
    if x - total_big < 0:
        times_in = x // 5
        if x - (times_in * 5) <= total_small:
            return True
        else:
            return False

# Course solution:

# def chocolate_maker(small, big, x):
#     if small + (5 * big) < x:
#         return False
#     if x % 5 > small:
#         return False
#     return True
