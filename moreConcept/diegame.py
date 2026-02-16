import random
print("warm welcome to the die game")
print("press `Enter` to roll the die or `q` to quit the game")

while True:
    user_input = input("Roll the die: ")
    if user_input.lower() == 'q':
        print("Thanks for playing the die game. Goodbye!")
        break
    elif user_input == '':
        die_roll = random.randint(1, 6)
        print(f"You rolled a {die_roll}!")
    else:
        print("Invalid input. Please press `Enter` to roll the die or `q` to quit the game.")

        