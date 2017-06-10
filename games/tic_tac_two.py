BOARD = """
       |       |       
       |       |       
____|____|____
       |       |       
       |       |       
____|____|____
       |       |       
       |       |       
       |       |       
"""

def player_turn(moves):
    move = input("Choose a quadrant from 1-9.\n")
    through_ten = [str(x) for x in range(1, 10)]
    while (move not in through_ten) or moves[int(move) - 1] != '  ' :
    # input validation
        print("That is not an available move.")
        move = input("Choose a quadrant between 1-9\n")
    return int(move)


def print_board(moves):
    for index, line in enumerate(BOARD.split("\n")):
        if index == 2:
            line = "   {}  |   {}  |   {}".format(moves[0], moves[1], moves[2])
        elif index == 5:
            line = "   {}  |   {}  |   {}".format(moves[3], moves[4], moves[5])
        elif index == 8:
            line = "   {}  |   {}  |   {}".format(moves[6], moves[7], moves[8])
        print(line)


def computer_turn(moves, computer):
    for i in range(9):          # check all quadrants
        if moves[i] == '  ':        # make sure space is blank
            for team in ('x', 'o'):  # check both teams
                copy =  moves[:]
                copy[i] = team
                if game_win(copy, team):
                    return i
            if i in (0, 2, 6, 8):
                return i
    if moves[i] == '  ':
        return i
            
def board_full(moves):
    return all(x != '  ' for x in moves)

def main(wins, games):
    turns = 0
    team = 's'
    moves = ['  ']*9
    while team != 'x' and team != 'o':       # choose a team
        team = input("Do you want to be X or O?\n").lower()
        if team == 'x':
            print("You will go first.")
            computer = 'o'
        elif team == 'o':
            print("The computer will go first.")
            computer = 'x'
            moves[ computer_turn(moves, computer) ] = computer
        else:
            print("Please type 'X' or 'O', or press Ctrl+D to exit.")
    while not (game_win(moves, team) or game_win(moves, computer) or board_full(moves)):
    # secondary loop
        print_board(moves)
        moves[ player_turn(moves) - 1] = team
        turns += 1
        if '  ' not in moves:     # board is full
            break
        moves[ computer_turn(moves, computer) ] = computer
    print_board(moves)
    if game_win(moves, team):
        print("You won! You beat the computer in {} turns.".format(turns))
        wins += 1
    elif game_win(moves, computer):
        print("You lost. The computer beat you in {} turns.".format(turns))
    else:
        print("The game ended in a tie.")
    games += 1
    print("You have won {} times and played a total of {} games.".format(wins, games))
    if input("Do you want to play again?\n").startswith('y'):
        main(wins, games)
    else:
        quit()


def game_win(moves, team):
#this is so clunky
    return ( (moves[0]==moves[3]==moves[6] ==team)  #left column
    or (moves[0]==moves[1]==moves[2] ==team)        #top row
    or (moves[0]==moves[4]==moves[8]==team)         #diagonal
    or (moves[6] == moves[4] == moves[2] == team)   # other diagonal
    or (moves[1]==moves[4]==moves[7] == team)       #middle column
    or (moves[3]==moves[4]==moves[5]==team)         #middle row
    or (moves[2]==moves[5]==moves[8]==team)         #right column
    or (moves[6]==moves[7]==moves[8]==team))        #bottom row


if __name__ == "__main__":
    print("""
       |       |       
 Tic |   2  |   3
____|____|____
       |       |       
4     |Tac |    6
____|____|____
       |       |       
7     |  8   | Toe
       |       |       
""") #looks nicer with two line breaks at end
    print("Version: 1.0.0")
    print("Welcome to Tic Tac Toe!")
    games = 0
    wins = 0
    print("""
How to play:
Choose a quadrant from 1-9.
Quadrants are numbered from left to right, top to bottom, like a book.
For example, quadrant 6 is the center-right square, and quadrant 7 is the bottom-left.""")
    main(games, wins)


