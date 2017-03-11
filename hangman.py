from random import randint
from linecache import getline
from shutil import get_terminal_size
PICTURES = ['''

 +---+
 |   |
     |
     |
     |
     |
==========''', '''

 +---+
 |   |
 O   |
     |
     |
     |
==========''', '''

 +---+
 |   |
 O   |
 |   |
     |
     |
==========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
==========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
==========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
==========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
==========''', '''

 +---+
 ^   |
 O   |
/|\  |    GAME
/ \  |    OVER
     |
==========''']
def randword(min_length, max_length, dictionary):
#american-english-small can be replaced with american-english[-large|-huge]
    DICT = open(dictionary, 'r')
    word = getline(dictionary, randint(1, len(DICT.readlines()))).strip()
    DICT.close()
    if (len(word) > max_length) or (len(word) < min_length) or ("'" in word):
        word = randword(min_length, max_length)
    return word
def showBoard(secretWord, errors, correctGuesses):
    try:
        print(PICTURES[len(errors)] + "\n")
    except IndexError:
        print(PICTURES[5] + "\n")
    blanks = ("_" * len(secretWord))
    for i in range(len(secretWord)):
        if secretWord[i] in correctGuesses:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]
    for letter in blanks:
        print(letter, end=' ')
    print()
    if not (errors == []):
        print("Incorrect guesses: ", end="")
        for x in errors:
            print(x, end=" ")
def getGuess(errors, correctGuesses, NOTLETTERS):
    while True:
        guess = input("\nGuess a letter.\n").lower()
        inputError = False
        for x in NOTLETTERS:
            if x in guess:
                print("That is not a letter.")
                inputError = True
        if len(guess) > 1:
            print("Please only type letters.")
            inputError = True
        elif guess in errors or guess in correctGuesses:
            print("You've already guessed that.")
            inputError = True
        if inputError == False:
            return guess
#ideas: 2-player; word can be selected
#       easy, medium, hard = length of word
#       remove caps, conjuctions
def main():
    NOTLETTERS = """1234567890-=!@#$$%^&*() _+`~,./<>?;':"[]\{}|"""
    gameWin = False
    errors = []
    correctGuesses = []
    correct = 0
    secretWord = 'error'
    game_type = input("Would you like to play against the computer or a friend? " +
             "[[computer|friend]\n").lower()
    while secretWord == 'error':
        if game_type.startswith('c'):
            difficulty = input("Easy, medium, or hard? " +
                               "(This option controls the length of the word)\n")
            min_length = -1
            while min_length == -1:
                if difficulty.startswith('h'):
                    min_length = 7
                    max_length = 100
                    dictionary = "/usr/share/dict/american-english-huge"
                elif difficulty.startswith('m'):
                    min_length = 4
                    max_length = 8
                    dictionary = "/usr/share/dict/american-english"
                elif difficulty.startswith('e'):
                    min_length = 0
                    max_length = 6
                    dictionary = "/usr/share/dict/american-english-small"
                else:
                    difficulty = input("Sorry, I don't understand. " +
                                       "Easy, medium, or hard?\n")
            secretWord = randword(min_length, max_length, dictionary)
        elif game_type.startswith('f'):
            secretWord = input("Please enter a word for your friend to guess. " +
                               "The screen will clear after you press enter.\n")
#doesn't work in python shell        print("\n" * get_terminal_size().lines)
            print("\n" * 50)
        else:
            game_type = input("Sorry, I didn't recognize that option. " +
                  "Please type 'c' for computer or 'f' for friend.\n")
    while True:
        showBoard(secretWord, errors, correctGuesses)
        guess = getGuess(errors, correctGuesses, NOTLETTERS)
        if guess in secretWord or guess == secretWord:
            print("Good guess!")
            correctGuesses.append(guess)
            correct+=1
            if correct == len(secretWord):
                print("You've won! Congratulations!")
                break
        else:
            print("Sorry, that's incorrect.")
            errors += guess
        if len(errors) >= len(PICTURES)-1 :
            showBoard(secretWord, errors, correctGuesses)
            print("\nYou've run out of guesses. \nYou had " + str(len(errors)) +
                  " errors and " + str(len(correctGuesses)) + " correct guesses. " +
                  "\nThe word was " + secretWord + ".")
            break
    play = input("Play again?\n").lower().strip()
    while True:
        if play.startswith('y'):
            main()
        elif play.startswith('n'):
            quit()
        else:
            play = input("Sorry, I only accept yes or no values. Play again?\n").lower().strip()
print("H A N G M A N")
print("_ _ _ _ _ _ _")
main()
