from random import randint

for x in range(1,6):
    guessnumber = int(input("Enter your guss between 1 to 5:  "))
    randomNumber = randint(1, 5)

    if guessnumber == randomNumber:
        print("You are won")
    else:
        print("You lose")
        print("Random number was:  ", randomNumber)
