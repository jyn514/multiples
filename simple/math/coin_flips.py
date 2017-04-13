from random import randint
def main():
    times = 0
    while times == 0:
        try:
            times = int(input("How many times would you like to flip a coin?\n"))
            if times == 0:
                print("Exiting program.")
                quit()
        except ValueError:
            print("I didn't recognize that as a number. Starting over.")
    tails = 0
    heads = 0
    n=0
    print("Flipping virtual coins . . .")
    while n < times:
        if randint(0, 1):
            heads+=1
        else:
            tails+=1
        n+=1
    print("Success! \nNumber of heads:" + str(heads)
          + "\nNumber of tails: " + str(tails))
    if input("Play again?\n") in ['yes', 'y']:
        main()
main()
quit()
