# Practicing writing comments and docstrings.

def func(num1, num2):
    """
    Calculates the sum of two numbers.
    :param num1: first number value
    :param num2: second number value
    :type num1: float / int
    :type num2: float / int
    :return: The sum of two numbers
    :rtype: float / int
    """
    sum_nums = num1 + num2
    return sum_nums


def main():
    # This program sums two numbers and return the value back
    func(4, 6)
    print(func(3, 7))


if __name__ == "__main__":
    main()

help(func)
