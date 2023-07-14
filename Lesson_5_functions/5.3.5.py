#


def distance(num1, num2, num3):
    absulut1_3_1 = abs(num3 - num1)
    absulut1_2_1 = abs(num2 - num1)
    absulut2_3_2 = abs(num3 - num2)
    absulut_2_2_3 = abs(num2 - num3)
    if absulut1_2_1 == 1 or absulut1_3_1 == 1:
        if absulut_2_2_3 >= 2 and absulut1_2_1 >= 2:
            return True
        elif absulut2_3_2 >= 2 and absulut1_3_1 >= 2:
            return True
    return False
print(distance(1, 2, 10))
print(distance(4, 5, 3))
print(distance(1, 2, 3))
print(distance(-1, -2, 10))
print(distance(0, 5, -5))
# Course solution:

# def distance(num1, num2, num3):
#     return ((abs(num1-num2) <= 1 or abs(num1-num3) <= 1)
#            and ((abs(num3-num2) >= 2 and abs(num1-num3) >= 2)
#            or (abs(num1-num2) >= 2 and abs(num2-num3) >= 2)))
