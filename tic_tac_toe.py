from time import sleep
BOARD = """
    |    |    
    |    |    
____|____|____
    |    |    
    |    |    
____|____|____
    |    |    
    |    |    
    |    |    
"""

moves = ["none"]*9
turns = 0
print("""Tic\n      Tac\n               Toe""")
team = input("Do you want to be X or O?\n").lower()
if team == "x":
    print("You will go first.")
    team = x
elif team == 'o':
    print("The computer will go first.")
    team = o
    sleep(1)
# computer moves once I get around to programming it
else:
    print("Please type 'X' or 'O', or press Ctrl+D to exit.")
move = input("Choose a quadrant from 1-9. Quadrants are numbered from left to right, " +
      "top to bottom, like a book. \nFor example, quadrant 6 is the " +
      "center-right square, and quadrant 7 is the bottom-left.\n")    
while True: 
    drawBoard(board, moves)
    move = input("Choose a quadrant from 1-9.\n")
    moves[move] = team
#   computer moves
    turns += 1
    if not gameOver():
        break
print("Thank you for playing. Come again some time!")
sleep(3)

def drawBoard(board, moves):
    
    for x in range(1, 10):
        print("{}|{}|{}").format(myformat(moves, x))

def gameOver():
    if not #evaluate game over :
        return True
    elif #evaluate game win :
        print("You won! You beat the computer in {} turns.".format(turns))
    elif #evaluate game loss :
        print("You lost. The computer beat you in {} turns.".format(turns))
    else:
        print("The game run into an unexpected error. Please contact the " +
              "programmer and bash him on the head, but not too hard.")
    play_again = input("Would you like to play again?\n")
    if play_again.lower().startswith('y'):
        moves = ['none']*9
        turns = 0
        return True
    else:
        quit()
        
def myformat(moves, line):
# there's got to be a better way to do this
    if line in [1, 4, 7]:
        if moves[self.quadrant] == x:
            return "\  /"
        elif moves[self.quadrant] == o:
            return " oo "
        elif moves[self.quadrant] == "none"
            return "    "
    elif line in [2, 5, 8]:
        if moves[self.quadrant] == x:
            return " xx "
        elif moves[self.quadrant] == o:
            return "o  o"
        elif moves[self.quadrant] == "none"
            return "    "
    elif line in [3, 6]:
        if moves[self.quadrant] == x:
            return "/__\"
        elif moves[self.quadrant] == o:
            return "o__o"
        elif moves[self.quadrant] == "none"
            return "____"
    elif line == 9:
        if moves[self.quadrant] == x:
            return "/__\"
        elif moves[self.quadrant] == o:
            return "o__o"
        elif moves[self.quadrant] == "none"
            return "    "        
    else:
        print("Fatal error. Please bash the programmer on the head, but not too hard or he won't fix the problem.")

def gameFinish(moves):
    if ( (moves[1]==moves[4]==moves[7] and not(moves[1]=='none') )
    or (moves[1]==moves[2]==moves[3] and not moves[1]=='none')
    or (moves[1]==moves[5]==moves[9]) and not moves[1]=='none'
    or (moves[2]==moves[5]==moves[7])
