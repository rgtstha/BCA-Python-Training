import random

def guess_the_number(difficulty):
    match difficulty:

      # user picks the difficulty
      # based on difficulty choosed by the users, value are assigned 

        case "easy":
            lower_bound, upper_bound, max_attempts = 1, 20, 5
        case "medium":
            lower_bound, upper_bound, max_attempts = 1, 50, 8
        case "hard":
            lower_bound, upper_bound, max_attempts = 1, 100, 10
        case _:
            print("Invalid difficulty level. Please choose from easy, medium, or hard.")
            return



    #this line of generates the random number
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Welcome to Guess the Number ({difficulty.capitalize()} level)!")
    print(f"You have {max_attempts} to guess the number")

    while attempts < max_attempts:
      
        user_guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
        attempts += 1

        if user_guess < target_number:
            print("Too low! Try again.")
        elif user_guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            return

    print(f"Sorry, you've used all {max_attempts} attempts. The number was {target_number}.")

# Choose difficulty level
difficulty_level = input("Choose difficulty level (easy, medium, hard): ")
guess_the_number(difficulty_level.lower())

