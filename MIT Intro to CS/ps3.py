import random

"""Two-player game, goes at beginning of play_game()
    player1_name = input("What is your name?\n>>")
    player2_name = input("What is your friend's name?\n>>")
    stdin = ''
    while stdin == '':     
        print("Would you like to play against the computer or a friend?")
        stdin = input(">>").lower()
        if stdin.startswith('c'):
            game = 'computer'
        elif stdin.startswith('f'):
            game = 'friend'
        else:
            print("Sorry, I only acce
"""

def score(word):
    total = 0
    for char in word.lower():
        total += VALUE[char]
    total *= len(word)
    if len(word)==hand_size:
        total += 50
    return total

def import_words():
    print("Loading dictionary file . . . ")
    dict_file = open(DICT, 'r', 1, 'UTF-8')
    wordlist = []
    for line in dict_file:
        if "'" not in line:
            wordlist.append(line.strip().lower())
    print("   {} words loaded.".format(len(wordlist)))
    dict_file.close()
    return wordlist

def show_hand(hand):
    for letter in hand.keys():
        for n in range(hand[letter]):
            print(letter, end=" ")
    print()

def deal_hand():
    hand = dict()
    for n in range(hand_size):
        letter = LETTERS[random.randrange(0, len(LETTERS))]
        hand[letter] = hand.get(letter, 0) + 1
    return hand

def update_hand(hand, word):
    #must be run after is_valid_word(); assumes all letters are present in hand
    for letter in word:
        hand[letter] -=1
    return hand

def is_valid(word, hand, wordlist):
    if word == '.':
        raise KeyError
    for letter in word:
        if hand.get(letter, 0) == 0:
            raise KeyError
    if word in wordlist:
        return True
    else:
        return False

def hand_length(hand):
#can I make hand a class?
    length = 0
    for v in hand.values():
        length += v
    return length

def input_word(hand):
    valid = False
    print("Letters in your hand: ", end="")
    show_hand(hand)
    word = input("Play a word: ")
    while not valid:
        try:
            valid = is_valid(word, hand, word_list)
            if valid == False:
                word = input("That word isn't in my dictionary. Try a different word: ")
        except KeyError:
            if word == ".":
                raise KeyError
            word = input("You tried to make a word with letters that aren't in your hand. Try a different word: ")
    return word

def play_hand(hand, word_list):
    hand_score = 0
    while hand_length(hand) > 0:
        try:
            word = input_word(hand)
            print("Good word! You scored {} points. ".format(score(word)))
            print("You can play another word, or type '.' to end your turn.")
            hand_score+=score(word)
            hand = update_hand(hand, word)
        except KeyError:
            print("Your turn is over.")
            return hand_score
    return hand_score

def play_game(word_list):
    total_score = 0
    while True:
        total_score += play_hand(deal_hand(), word_list)
        print("\nYou've scored {} points so far.".format(total_score))
        stdin = input("Type 'h' to play a new hand, 'n' to play a new game, or 'e' to exit.\n>>").lower()
        while True:
            if stdin.startswith('n'):
                play_game(word_list)
            elif stdin.startswith('h'):
                break
            elif stdin.startswith('e'):
                raise SystemExit
            stdin = input("Sorry, I only take 'n', 'h', or 'e' as answers. Play again?\n>>").lower()  
hand_size = 7
VALUE = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '':0
}

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
#Feel free to change this dictionary to reduce load times
DICT = "/usr/share/dict/american-english-small"

if __name__ == '__main__':
    word_list = import_words()
    print("Hello! Welcome to bananagrams.")
    while True:
        stdin = input("Type 'n' to play a new game, or type 'e' to exit.\n>>")
        if stdin == 'n':
            play_game(word_list)
        elif stdin == 'e':
            raise SystemExit
        else:
            stdin = input("Sorry, I only accept 'n' or 'e'. Type 'n' to play a new game, or type 'e' to exit. " +
                          "If for some reason 'e' isn't working, press Ctrl+C to exit the module or Ctrl+D to force-close.")
            
