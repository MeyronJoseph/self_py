def main():
    data = ("self", "py", 1.543)
    format_string = "Hello %s.%s learner, you have only %3.3s \
units left before you master the course!"
    print(format_string % data)


if __name__ == "__main__":
    main()


# Course solution:


# data = ("self", "py", 1.555)
# format_string = "Hello %s.%s learner, you have only %.3s units left before you master the course!"
#
# print(format_string % data)
