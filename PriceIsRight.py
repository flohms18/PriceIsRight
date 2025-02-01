import random

def PickRandomNumber():
    IntToGuess = random.randint(1,100)
    while True : 
        try:
            IntUser = int(input("Guess the number between 1 & 100 : "))
            if IntUser < IntToGuess:
                print("Too Low ! Pick Again!")
            elif IntUser > IntToGuess:
                print("Too High ! Pick Again!")
            else :
                print("Congrats ! You have found the right number:")
                print(IntToGuess)
                break
        except ValueError:
            print("Invalid Number")


PickRandomNumber()
        



