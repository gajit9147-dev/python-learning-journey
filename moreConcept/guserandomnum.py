import random

num = random.randint(1, 20)
max_attempts = 10

for attempt in range(1, max_attempts + 1):
    user_input = input(f"Guess the number (attempt {attempt}/{max_attempts}): ")
    if user_input.isdigit():
        user_guess = int(user_input)
        if user_guess == num:
            print("Congratulations! You guessed the number correctly.")
            break
        elif user_guess < num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        remaining = max_attempts - attempt
        if remaining:
            print(f"Attempts left: {remaining}")
    else:
        print("Invalid input. Please enter a valid number.")
        remaining = max_attempts - attempt
        if remaining:
            print(f"Attempts left: {remaining}")
else:
    print(f"Better luck next time! The correct number is {num}.")
        

        