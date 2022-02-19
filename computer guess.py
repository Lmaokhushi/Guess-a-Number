import random

x = int(input("Enter the number that you want the computer to guess out of : "))

c = int(input(f"Enter a number between 1 to {x} that you want the computer to guess : "))

def computer_guess(x):
    for y in range(1, x):
       guess = random.randint(1, x)
       if guess == c:
        quit()
       elif guess > c:
        print(f"Sorry, my guess {guess} is too high")
        continue
       elif guess < c:
        print(f"Sorry, my guess {guess} is too low")
        continue
    print(f"The computer has guessed the number {c} correctly!!")

computer_guess(x)