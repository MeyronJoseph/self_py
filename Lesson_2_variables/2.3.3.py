# Need to add an explanation :)


digits = int(input("Enter three digits (each digit for one pig: "))
p_one = digits//100
p_two = (digits % 100) // 10
p_three = (digits % 100) % 10

sum_bricks = p_one + p_two + p_three
each_p = sum_bricks // 3
module_p = sum_bricks % 3
bool_p = module_p == 0

print(sum_bricks)
print(each_p)
print(module_p)
print(bool_p)


# Course answer:

# def main():
#     string_num = input("enter a digit number")
#     bricks = sum([int(num) for num in string_num])
#     print(bricks)
#     print(int(bricks / 3))
#     print(bricks % 3)
#     print(bricks % 3 == 0)
#
#
# if __name__ == "__main__":
#     main()
