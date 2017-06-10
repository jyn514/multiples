from random import randint
from time import sleep

INTRO = """You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight."""

CAVE = """You approach the cave...
It is dark and spooky...
A large dragon jumps out in front of you! He opens his jaws and..."""

BAD = "Gobbles you down in one bite!"
GOOD = "Gives you his treasure!"

def main(treasure):
    print(INTRO)
    choice = 0
    while choice != '1' and choice != '2':
        choice = input("Which cave will you go into? (1 or 2)\n")
    for line in CAVE.split("\n"):
        print(line)
        sleep(2)
    if choice == str(randint(1, 2)):
        print(GOOD)
        treasure += 1
    else:
        print(BAD)
    sleep(2)
    print("Total treasure collected: " + str(treasure))
    if input("Play again? (y or n)\n").startswith('y'):
        main(treasure)

if __name__ == "__main__":
    treasure = 0
    main(treasure)
