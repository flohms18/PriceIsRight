import random

def PickRandomNumber():
    IntToGuess = random.randint(1,100)
    IntUser = input("Pick a number between 1 & 100: ")
    if IntToGuess < int(IntUser) :
        print("Too High! Pick Again!")
        IntUser = input("Pick a number between 1 & 100: ")

    elif IntToGuess > int(IntUser) :
        print("Too Low! Pick Again!")
        IntUser = input("Pick a number between 1 & 100: ")

    else:
        print("Good Guess! Congrats!")
        return IntToGuess

PickRandomNumber()
        



