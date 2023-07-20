def main():
    """
    7 options to the user choose.
    Each option prints or makes something with the dict
    :return: depends on the user choice
    """
    my_dictionary = {"first_name": "Mariah",
                     "last_name": "Carey",
                     "birth_date": "27.03.1970",
                     "hobbies": ["Sing", "Compose", "Act"]}

    player_input = input("Please enter a number between 1-7: ")

    if player_input == "1":
        mariah_last_name = my_dictionary["last_name"]
        print(mariah_last_name)

    elif player_input == "2":
        mariah_birth_day = my_dictionary["birth_date"]
        print(mariah_birth_day)

    elif player_input == "3":
        hobbies_len = len(my_dictionary["hobbies"])
        print(hobbies_len)

    elif player_input == "4":
        last_hobby = my_dictionary["hobbies"][2]
        print(last_hobby)

    elif player_input == "5":
        new_hobbies = ["Sing", "Compose", "Act", "Cooking"]
        my_dictionary["hobbies"] = new_hobbies

    elif player_input == "6":
        the_birth_day = my_dictionary["birth_date"]
        birth_day_list = the_birth_day.split(".")
        birth_day_tuple = tuple(birth_day_list)
        print(birth_day_tuple)

    elif player_input == "7":
        my_dictionary["age"] = 2022 - 1970
        print(my_dictionary["age"])

    else:
        "Please choose a correct number! "


if __name__ == "__main__":
    main()


# Course solution:


# mariah = {
#     "first_name": "Mariah",
#     "last_name": "Carey",
#     "birth_date": "27.03.1970",
#     "hobbies": ["Sing", "Compose", "Act"]
# }
# command = int(input("Enter a command: "))
# if command == 1:
#     print(mariah["last_name"])
# if command == 2:
#     print(mariah["birth_date"][3:5])
# if command == 3:
#     print(len(mariah["hobbies"]))
# if command == 4:
#     print(mariah["hobbies"][-1])
# if command == 5:
#     mariah["hobbies"].append("Cooking")
# if command == 6:
#     mariah["birth_date"] = (int(mariah["birth_date"][:2]), int(mariah["birth_date"][3:5]), int(mariah["birth_date"][-4:]))
#     print(mariah["birth_date"])
# if command == 7:
#     mariah['age'] = 2021 - int(mariah["birth_date"][6:])
#     print(mariah["age"])
