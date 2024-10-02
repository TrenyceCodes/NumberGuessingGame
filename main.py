#variables
import random

def runNumberGuessingGame():
    number_of_guesses = 7

    while number_of_guesses > 0:
        try:
            user_guess = int(input("Guess a number 1-10: "))
            random_num_guess = random.randint(1, 10)

            if user_guess == random_num_guess:
                print("You guessed the right number")
                break
            elif user_guess != random_num_guess:
                number_of_guesses -= 1
                print(f"number of guesses left: {number_of_guesses}")
                print("Try again! Wrong Number")
                if user_guess > random_num_guess:
                    print("You guessed too high try again")
                else:
                    print("You guessed too low try again")
        except ValueError:
            print("Please enter number between 1-10.")
            continue

    if number_of_guesses == 0:
        print("Game Over! You have run out of guesses.")

#runs the script directly
if __name__ == "__main__":
    runNumberGuessingGame()