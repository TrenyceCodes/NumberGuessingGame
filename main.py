#variables
import random

def runNumberGuessingGame():
    global number_of_guesses
    number_of_guesses = 3

    while number_of_guesses != 0:
        try:
            user_guess = int(input("Guess a number 1-10: "))
            random_num_guess = random.randint(1, 10)

            if number_of_guesses == 0:
                break

            if user_guess == random_num_guess:
                print("You guessed the right number")
                break
            elif user_guess != random_num_guess:
                number_of_guesses -= 1
                print(f"number of guesses left: {number_of_guesses}")
                print("Try again! Wrong Number")
        except ValueError:
            print("Please enter number between 1-10.")

#runs the script directly
runNumberGuessingGame()