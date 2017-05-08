from random import randint

def game(name, minimum, maximum):
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
    return tries

def main():
    name = input("Hello! What is your name?\n")
    played = 0
    high_score = [None]*3
    while True:
        difficulty = input("Would you like to play an easy, medium, or hard game? You can also 'exit' or 'quit'.\n")
        while difficulty not in ['easy', 'e', 'm', 'medium', 'hard', 'h', 'exit', 'quit']:
            difficulty = input("Sorry, I don't recognize what you typed.\n")
        if difficulty == 'easy' or difficulty == 'e':
            minimum = 1
            maximum = 20
            new = game(name, minimum, maximum)
            if high_score[0] == None:
                high_score[0] = new
            elif new < high_score[0] :
                high_score[0] = new
        elif difficulty == 'medium' or difficulty == 'm':
            minimum = 0
            maximum = 50
            new = game(name, minimum, maximum)
            if high_score[1] == None:
                high_score[1] = new
            elif new < high_score[1]:
                high_score[1] = new
        elif difficulty == 'hard' or difficulty == 'h':
            minimum = -100
            maximum = 100
            new = game(name, minimum, maximum)
            if high_score[2] == None:
                high_score[2] = new
            elif new < high_score[2]:
                high_score[2] = new
        elif difficulty in ['exit', 'quit', 'no', 'stop']:
            quit()
        print("Your current high scores are: ")
        print("Easy: {}".format(high_score[0]).center(4))
        print("Medium: {}".format(high_score[1]).center(4))
        print("Hard: {}".format(high_score[2]).center(4))
        

if __name__=="__main__":
    main()
