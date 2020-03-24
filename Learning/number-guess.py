from random import randint
play = True

#Function to choose a random number
def get_random():
    print("\nThe computer has choosen a number between 1 and 100.\n")
    target = (randint(1,100))
    return target

#Function asks player for a guess(input)
def take_guess():
    try:
        guess = int(input("What do you think it is?\n"))
    except ValueError:
        print("You must enter a number between 1 and 100!")
    else:
        if guess < 0 or guess > 100:
            print("You must enter a number between 1 and 100!")
        else:
            return guess

#Function compares the guess of the player to the target number
def compare_guess(target, guess):
    if guess > target:
        print("Your guess is too high!")
    elif guess < target :
        print("Your guess is too low!")
    else:
        print("Bingo! You guessed correctly!")

#while loop that plays the game
while play:
    target = get_random()
    guess = take_guess()
    compare_guess(target, guess)
