import random

def computer_guess(x):
    low = 1
    high = x
    reply = ''
    while reply != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        reply = input(f'Is the {guess} high (type h), low(type l), or correct (tupe c)')
        if reply == 'h':
            high = guess - 1
        elif reply == 'l':
            low = guess + 1
        elif reply == 'c':
            break
    print("you have guessed the number correctly")

computer_guess(10)