from random import randint
import linecache
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
==========''']
def randword():
#american-english-small can be replaced with american-english[-large|-huge]
    DICT = open('/usr/share/dict/american-english-small', 'r')
    word = linecache.getline('/usr/share/dict/american-english-small', randint(1, len(DICT.readlines())))
    DICT.close()
    return word.strip().replace("'", "")
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
        
def main():
    NOTLETTERS = """1234567890-=!@#$$%^&*()_+`~,./<>?;':"[]\{}|"""
    gameWin = False
    errors = []
    correctGuesses = []
    secretWord = randword()
    while True:
        showBoard(secretWord, errors, correctGuesses)
        guess = getGuess(errors, correctGuesses, NOTLETTERS)
        if guess in secretWord or guess == secretWord:
            print("Good guess!")
            correctGuesses.append(guess)
            if "".join(correctGuesses) == secretWord:
                print("You've won! Congratulations!")
                break
        else:
            print("Sorry, that's incorrect.")
            errors += guess
        if len(errors) > len(PICTURES)-1 :
            showBoard(secretWord, errors, correctGuesses)
            print("\nYou've run out of guesses. \nYou had " + str(len(errors)) +
                  " errors and " + str(len(correctGuesses)) + " correct guesses. " +
                  "\nThe word was " + secretWord + ".")
            break
    if input("Play again?\n").lower().startswith('y'):
        main()
print("H A N G M A N")
print("_ _ _ _ _ _ _")
main()
quit()
