# My solution:


# print("""
# Please write a grocery list separated by commas and no spaces
# For example: Milk,Tomato,Honey,Bananas
# """)
# user_grocery_string = input("Write your grocery list here >>> ")
# user_grocery_input = user_grocery_string.split(",")
# user_grocery_list = []
# for item in user_grocery_input:
#     item = item.title()
#     item = item.strip()
#     user_grocery_list.append(item)
#
# message = """
# Excellent! Now this are your options:
#
# 1 >>> Show your grocery list
# 2 >>> Numbers of items in the list
# 3 >>> Check if an item is in the grocery list
# 4 >>> Check how many times an item is in the list
# 5 >>> Delete an item
# 6 >>> Add an item
# 7 >>> Show the illegal items (length less than 3 or no "abc" chars
# 8 >>> Remove all existing duplicates in the list
# 9 >>> Exit
# """
# print(message)
#
# while True:
#     user_number_choice = input("Type a number: ")
#     match user_number_choice:
#         case "1":
#             print(user_grocery_list)
#
#         case "2":
#             list_length = len(user_grocery_list)
#             print(list_length)
#
#         case "3":
#             is_item_in_list = input("Type an item name to check existences: ")
#             is_item_in_list = is_item_in_list.title()
#             is_item_in_list = is_item_in_list.strip()
#             if is_item_in_list in user_grocery_list:
#                 print(f"The item {is_item_in_list} exist in the list.")
#             else:
#                 print(f"The item {is_item_in_list} does not exist in the list.")
#
#         case "4":
#             item_name_count = input("Type item name to count: ")
#             item_name_count = item_name_count.strip()
#             item_name_count = item_name_count.title()
#             item_count = user_grocery_list.count(item_name_count)
#             print(item_count)
#
#         case "5":
#             try:
#                 item_name_exist = input("Type item name to remove: ")
#                 item_name_exist = item_name_exist.title()
#                 item_name_exist = item_name_exist.strip()
#                 user_grocery_list.remove(item_name_exist)
#             except ValueError:
#                 print("Please write an item that exist in the list.")
#
#         case "6":
#             item_to_add = input("Type an item to add to the grocery list: ")
#             item_to_add = item_to_add.title()
#             item_to_add = item_to_add.strip()
#             user_grocery_list.append(item_to_add)
#
#         case "7":
#             for item in user_grocery_list:
#                 if not(item.isalpha()) or len(item) < 3:
#                     print(item)
#
#         case "8":
#             user_grocery_list = list(set(user_grocery_list))
#
#         case "9":
#             print("Thank you and goodbye!")
#             break
#
#         case _:
#             msg = "Please type in correctly! "
#             continue

##############################################################################################

# Rubi Chat solution:

# def print_products(products):
#     print("Products:", ", ".join(products))
#
#
# def print_product_count(products):
#     print("Number of products:", len(products))
#
#
# def is_product_in_list(products, product):
#     if product in products:
#         print("Product", product, "is in the list.")
#     else:
#         print("Product", product, "is not in the list.")
#
#
# def count_product_occurrences(products, product):
#     count = products.count(product)
#     print("Product", product, "appears", count, "time(s) in the list.")
#
#
# def remove_product(products, product):
#     if product in products:
#         products.remove(product)
#         print("Product", product, "removed from the list.")
#     else:
#         print("Product", product, "is not in the list.")
#
#
# def add_product(products, product):
#     products.append(product)
#     print("Product", product, "added to the list.")
#
#
# def print_invalid_products(products):
#     invalid_products = [p for p in products if len(p) < 3 or not p.isalpha()]
#     if invalid_products:
#         print("Invalid products:", ", ".join(invalid_products))
#     else:
#         print("No invalid products found.")
#
#
# def remove_duplicates(products):
#     unique_products = list(set(products))
#     print("Duplicates removed.")
#     return unique_products
#
#
# def validate_product_list(products_str):
#     return [p.strip() for p in products_str.split(",")]
#
#
# def print_menu():
#     print("1. Print the list of products")
#     print("2. Print the number of products in the list")
#     print("3. Check if a product is in the list")
#     print("4. Check how many times a product appears in the list")
#     print("5. Delete a product from the list")
#     print("6. Add a product to the list")
#     print("7. Print all invalid products")
#     print("8. Delete duplicates")
#     print("9. Exit")
#
#
# def main():
#     products_str = input("Enter the list of products (comma-separated without spaces): ")
#     products = validate_product_list(products_str)
#
#     while True:
#         print_menu()
#         choice = int(input("Select an option (1-9): "))
#
#         if choice == 1:
#             print_products(products)
#         elif choice == 2:
#             print_product_count(products)
#         elif choice == 3:
#             product = input("Enter a product name: ")
#             is_product_in_list(products, product)
#         elif choice == 4:
#             product = input("Enter a product name: ")
#             count_product_occurrences(products, product)
#         elif choice == 5:
#             product = input("Enter a product name: ")
#             remove_product(products, product)
#         elif choice == 6:
#             product = input("Enter a product name: ")
#             add_product(products, product)
#         elif choice == 7:
#             print_invalid_products(products)
#         elif choice == 8:
#             products = remove_duplicates(products)
#         elif choice == 9:
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
#     print("Exiting the program.")
#
#
# if __name__ == "__main__":
#     main()


# Some code I found on GitHub from "ekeydar" solution:


def main_loop(products):
    while True:
        choice = int(input('Please enter choices (1-9): '))
        if choice == 1:
            for product in products:
                print(product)
        elif choice == 2:
            print(len(products))
        elif choice == 3:
            product = input('Please enter product to check if in list: ')
            print(product in products)
        elif choice == 4:
            product = input('Please enter product to count: ')
            print(products.count(product))
        elif choice == 5:
            product = input('Please enter product to remove: ')
            if product in products:
                products.remove(product)
        elif choice == 6:
            product = input('Please enter product to add: ')
            products.append(product)
        elif choice == 7:
            for product in products:
                if not is_legal(product):
                    print(product)
        elif choice == 8:
            products = remove_dups(products)
            print('Duplicated removed')
        elif choice == 9:
            print('Bye')
            break


def is_legal(product):
    if len(product) < 3:
        return False
    for c in product:
        if c.lower() not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True


def remove_dups(products):
    result = []
    for p in products:
        if p not in result:
            result.append(p)
    return result


def main():
    products = input('Please enter products list: ')
    main_loop(products.split(","))


if __name__ == '__main__':
    main()


# Course solution:


# def main():
#     """Applies actions on list of items according to the input command.
#     first input: list of items, seperate by ','
#     second input: command number (1-9)
#     """
#     my_list=input("Enter grocery list: ").split(',')
#     command = None
#     while command != 9:
#         command = int(input("Enter command: "))
#         if command == 1:
#             print(my_list)
#         if command == 2:
#             print(len(my_list))
#         if command == 3:
#             check_for = input("check for an item: ")
#             print(check_for in my_list)
#         if command == 4:
#             check_for = input("count an item: ")
#             print(my_list.count(check_for))
#         if command == 5:
#             my_list.remove(input("remove an item: "))
#         if command == 6:
#             my_list.append(input("add an item: "))
#         if command == 7:
#             print([item for item in my_list if (len(item) <3 or not item.isalpha())])
#         if command == 8:
#             my_list= list(set(my_list))
#
#
# if __name__ == "__main__":
#     main()
