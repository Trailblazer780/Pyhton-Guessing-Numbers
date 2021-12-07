import math 
import random
import time

def getGuess(secretNumber):
    # Set initial variables and list need to run program correctly
    count = 1
    validGuess = False
    currentGuesses = []

    print("Number Guessing Game ---------------")

    # While the number of attempts to guess the number is 10 or under the program will run the code below. The count starts at 1.

    while (count <= 11):
        # gets input from user and if it is valid it will set the validGuess flag to True and continue to run the program.
        try:
            guess = int(input("Enter guess #" + str(count)+" between 1 and 100: "))
            validGuess = True

        # If the input is incorrect it will set the validGuess flag to False and not accept the input and will try again.
        except ValueError:
            print("Error the guess must be a number between 1 and 100")
            validGuess = False

        # While the validGuess is set to True the program will enter this loop to do error checking and check if the guesses are valid.
        while (validGuess == True):

            # If the guess is correct the program will tell them they won and wait 2 seconds and the program will restart.
            if (guess == secretNumber):
                count = count + 1
                currentGuesses.append(guess)
                print("You Win!")
                time.sleep(2)
                return

            # If the user surpasses 10 guesses it will tell them they lost the game and wait 2 seconds and the program will restart.
            elif (count >= 10):
                print("You Lose - Please try again")
                time.sleep(2)
                return

            # If the guess has already been guessed it will set the validGuess flag to False and tell the user they have already guessed that. The program will then ask for the input again, note that the guess will not be stored in the currentGuesses list.
            elif(guess in currentGuesses):
                print("You have already guess that number!")
                validGuess = False

            # If guess is more than 100 which would make it out of range it will set the validGuess flag to False and the program will then ask for input again, note that the guess will not be stored in the currentGuesses list.
            elif (guess > 100):
                print("Guess must be between 1 and 100")
                validGuess = False
            
            # If the guess is 0 or negative it will set the validGuess flag to False and the program will then ask for input again, note that the guess will not be stored in the currentGuesses list.
            elif (guess < 1):
                print("Guess must be a positive number")
                validGuess = False

            # If the guess is valid and it is higher than the secret number it will append the number to the currentGuesses list, add 1 to the count of how many attempts, and reset the validGuess flag to False to ask for the next input.
            elif (guess > secretNumber):
                print("%2s #%0s : %1s - %1s" % ("Guess",str(count),str(guess),"Lower!"))
                print("------------------------------------")
                count = count + 1
                currentGuesses.append(guess)
                validGuess = False

            # If the guess is valid and it is lower than the secret number it will append the number to the currentGuesses list, add 1 to the count of how many attempts, and reset the validGuess flag to False to ask for the next input.
            elif (guess < secretNumber):
                print("%2s #%0s : %1s - %1s" % ("Guess",str(count),str(guess),"Higher!"))
                print("------------------------------------")
                count = count + 1
                currentGuesses.append(guess)
                validGuess = False


def generateSectretNum():
    # Generating the secret number and making it available.
    secret = random.randint(1, 100)

    # Returning the secret number and passing it 
    return secret

def startGame():
   
   while True:   
        # Every time game starts it will have a new secret number to guess
        secretNumber = generateSectretNum()

        # Print the secret number for debugging purposes
        print(secretNumber)

        # Call the function for the user to start giving input once the random number has been selected 
        getGuess(secretNumber)


# Starting the game
startGame()