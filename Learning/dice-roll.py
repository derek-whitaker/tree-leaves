from random import randint
play = True

print("This is a dice rolling simulator.\n")

while play:

    #Starts by asking if you want to roll the dice or quit the program.
    #You can keep rollin the dice until you quit. 
    choice = input("Enter 'R' to roll the dice, or 'Q' to quit the program. \n")

    if choice.upper() == 'R':
        print("\nYou roll the dice!\n")
        print(randint(1,6))
        play = True
    elif choice.upper() == 'Q':
        print("\nYou have choosen to quit the program. Goodbye!\n")
        play = False
    else:
        print("Sorry, please try again.\n")
        continue
