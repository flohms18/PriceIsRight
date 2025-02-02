import random



def PriceisRight():
    Attempt = 0
    MaxAttempt = 3
    IntToGuess = random.randint(1,100)
    while Attempt < MaxAttempt : 
        try:
            IntUser = int(input("Guess the number between 1 & 100 : "))
            Attempt += 1
            if IntUser < IntToGuess:
                print("Too Low ! Pick Again!")
                Attempt += 1
            elif IntUser > IntToGuess:
                print("Too High ! Pick Again!")
            else :
                print("Congrats ! You have found the right number:")
                print(IntToGuess)
                print(Attempt)
                return
        except ValueError:
            print("Invalid Number")
    print("Too many attemps!Game Over")

PriceisRight()
        



