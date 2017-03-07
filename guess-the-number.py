from random import randint
name = input("Hello! What is your name?\n")

difficulty = input("Would you like to play an easy, medium, or hard game?\n")
while difficulty not in ['easy', 'e', 'm', 'medium', 'hard', 'h']:
    difficulty = input("Sorry, I don't recognize what you typed.\n")
if difficulty == 'easy' or difficulty == 'e':
    minimum = 1
    maximum = 20
elif difficulty == 'medium' or difficulty == 'm':
    minimum = 0
    maximum = 50
elif difficulty == 'hard' or difficulty == 'h':
    minimum = -100
    maximum = 100
print("Well, " + name + ", I am thinking of a number between "
      + str(minimum) + " and " + str(maximum) + ".")
num = randint(minimum, maximum)
correct = False
tries = 1
while not correct:
    guess = int(input("Take a guess.\n"))
    if guess == num:
        print("Good job, " + name + "! You guessed the number in "
              + str(tries) + " guesses.")
        correct = True
    else:
        if guess < num:
            error = "low"
        elif guess > num:
            error = "high"
        print("Your guess is too ", end="")
        print(error + ".")
    tries += 1
    
