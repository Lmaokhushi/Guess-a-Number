import random

def guess(a):
    number = random.randint(1,a)
    guess = 0
    while guess != number:
        guess = int(input(f"Guess a number between 1 and {a} :"))
        if guess > number:
            print ("guess again. Too high:(")
        elif guess < number:
            print ("guess again. Too low:(")
    print("Congratulation!! You have guessed the number correctly :)")

guess(20)