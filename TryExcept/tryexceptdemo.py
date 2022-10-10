import random

try:
    secretNumber = random.randint(1, 10)
    print('I am Thinking of a number between 1 and 5')

    # ask player to guess

    for guessesTaken in range(1, 4):
        print("Take a Guess.")
        guess = int(input())

        if guess < secretNumber:
            print("Your guess is too low")

        elif guess > secretNumber:
            print("Your guess is too high")
        else:
            break
    if guess == secretNumber:
        print("Good Job! You gussted Secret Number in " + str(guessesTaken) + ' Guesses!')
    else:
        print("Nope!! The number i was thinking was " + str(secretNumber))

except:
    print("Wrong Input")
