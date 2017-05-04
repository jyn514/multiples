'''how game should run:

#logo
#detailed instructions
#main game loop()
    #set values to null
    #chose x or o
    #secondary loop
        #print board
        #move
        #board
        #other player moves
        #break on win or loss
    #if win:
        #congrats
    #if loss:
        #sorry
    #play again?
    #if yes:
        #main game loop()
    #if no:
        quit()
        
functions:
    print board(moves)
    user plays(games)
    computer plays(moves)
    win(moves)

lists:
    moves

variables:
    games
    turns

'''
from time import sleep
def player_turn():
    try:
        if games ==0:
            move = int(input("Choose a quadrant from 1-9. Quadrants are numbered from left to right, " 
              "top to bottom, like a book. \nFor example, quadrant 6 is the "
              "center-right square, and quadrant 7 is the bottom-left.\n"))
        else:
            move = int(input("Choose a quadrant from 1-9.\n"))
    except:
        print("That is not a number between one and nine.\n"
                         "Please choose a quadrant from 1-9.\n")
        move = player_turn()
#haven't tested this recursion, if it does work i'll be very happy
    return move

def play_again():
    games += 1
#increments before printing because it starts at zero.
    print("You have played {} games.".format(games))
#bug: will print 'You have played 1 games' after first game
    if input("Do you want to play again?\n").startswith('y'):
        return True
    else:
        return False

def myformat(moves, line):
# there's got to be a better way to do this
    if line in [1, 4, 7]:
        if moves[line] == 'x':
            return "\  /"
        elif moves[line] == 'o':
            return " oo "
        elif moves[line] == 'none':
            return "    "
    elif line in [2, 5, 8]:
        if moves[line] == x:
            return " xx "
        elif moves[line] == o:
            return "o  o"
        elif moves[line] == "none":
            return "    "
    elif line in [3, 6]:
        if moves[line] == x:
            return "/__\b"
        elif moves[line] == o:
            return "o__o"
        elif moves[line] == "none":
            return "____"
    elif line == 9:
        if moves[line] == x:
            return "/__\b"
        elif moves[line] == o:
            return "o__o"
        elif moves[line] == "none":
            return "    "        
    else:
        print("Fatal error. Please bash the programmer on the head, but not too hard or he won't fix the problem.")

def gameWin(moves, team):
#this is so clunky
    if ( (moves[1]==moves[4]==moves[7] ==team)  #left column
    or (moves[1]==moves[2]==moves[3] ==team)      #top row
    or (moves[1]==moves[5]==moves[9]==team)      #diagonal
    or (moves[2]==moves[5]==moves[8] == team)     #middle column
    or (moves[4]==moves[5]==moves[6]==team)       #middle row
    or (moves[3]==moves[6]==moves[9]==team)       #right column
    or (moves[7]==moves[8]==moves[9]==team)) :    #bottom row
        return True
    else:
        return False

def main():
    turns = 0
    team = 'undecided'
    moves = ['none']*9
    while team == 'undecided':
        team = input("Do you want to be X or O?\n").lower()
        if team == 'x':
            print("You will go first.")
            computer = 'o'
        elif team == 'o':
            print("The computer will go first.")
            computer = 'o'
            moves[ computer_turn() ] = computer
            sleep(1)
        else:
            print("Please type 'X' or 'O', or press Ctrl+D to exit.")
    sleep(1)
    for line in range(1, 10):
        print("{}|{}|{}".format((myformat(moves, line))))
    moves[ player_turn() ] = team
    for line in range(1, 10):
        print("{}|{}|{}".format((myformat(moves, line))))
    moves[ computer_turn() ] = computer
    if game_win(player):
        print("You won! You beat the computer in  {} turns.".format(turns))
        if play_again():
            main()
        else:
            quit()
    if game_win(computer):
        print("You lost. The computer beat you in {} turns.".format(turns))
        if play_again():
            main()
        else:
            quit()

print("Tic\n                 Tac\n                                   Toe\n") #looks nicer with two line breaks at end
print("Version: 0.1.0")
print("Welcome to Tic Tac Toe! This is a text-based game against a rudimentary AI. \n"
      "The controls are responses to simple questions.")
games = 0

main()

""" just because I couldn't bear to delete it
BOARD = #triple quote
        |        |     
        |        |    
____|____|____
        |        |    
        |        |    
____|____|____
        |        |    
        |        |    
        |        |    
I promise it looked nicer in idle
"""

