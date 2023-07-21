def copy_file_content(source, destination):
    """

    :param source:
    :param destination:
    :return:
    """
    with open(source) as file:
        file_to_copy = file.read()

    with open(destination, "w") as file:
        updated_file = file.write(file_to_copy)

copy_file_content("lesson.txt", "testing.txt")
