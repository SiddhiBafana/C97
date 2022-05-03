import random

num = random.randint(1, 10)
guess = None
chances = 5

while guess != num :
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        break
    else : print("Try again")

