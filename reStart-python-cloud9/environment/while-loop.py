import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
isGuessRight = False
# 1. If the user has not guessed the correct answer, enter the loop.
while isGuessRight != True:
    # 2.  Ask the user for a guess.
    guess = input("Guess a number between 1 and 10: ")
    # 3.  Is the guess the correct number?
    # 4.  If the correct guess, tell the user it was the correct guess and exit the loop.
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    # 5.  If the wrong guess, tell the user it was the wrong guess and continue the loop.
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))