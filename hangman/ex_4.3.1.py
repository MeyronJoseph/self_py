# Dealing with wrong input from the player


player_guess_char = input("Guess a letter: ")
abc_letters = "abcdefghijklmnopqrstuvwxyz"
lower_guess = player_guess_char.lower()
guess_len = len(player_guess_char)

if guess_len == 1 and lower_guess in abc_letters:
    print(lower_guess)
elif lower_guess.isalpha():
    if guess_len > 1:
        print("E1")
elif guess_len == 1:
    print("E2")
else:
    print("E3")


# Course solution:

# char = input("Guess a letter:")
# right_size = len(char) == 1
# is_alpha = char.isalpha()
# if right_size and is_alpha:
#     print(char.lower())
# if not right_size and not is_alpha:
#     print("E3")
# if not right_size and is_alpha:
#     print("E1")
# if right_size and not is_alpha:
#     print("E2")
