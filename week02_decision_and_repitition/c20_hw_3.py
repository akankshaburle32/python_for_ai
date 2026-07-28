#  c20     que 3:
## Number guessing game khelo aur jeeto!

import random

secret = random.randint(1, 10)

guess = int (input ("Guess a no. (1-10): "))

if guess == secret:
    print("Congratulation! You won. ")

else:
    print("Sorry! You lost. ")
    print("The correct no. was:", secret)