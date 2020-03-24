# Credit: Amir A. Shabani
# https://stackoverflow.com/questions/44008489/dice-rolling-simulator-in-python#44009898

from random import randint
roll = True
while roll:
    print("You roll two dice...")
    print("You got", randint(1,6), "and", randint(1,6), ".")
    print("Do you want to roll again?")
    roll = ("y" or "yes") in input().lower()
