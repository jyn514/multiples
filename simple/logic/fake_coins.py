from sys import argv

def find_fake(a, b, desc):
    if desc == "right":
        return "{} is fake".format(a)
    elif desc == "left":
        return "{} is fake".format(b)
    elif desc == "equal":
        return "not enough info"

def take_input(*args):
    if not len(args)/3 == 0:
        return "Wrong number of arguments. Aborted."
    else:
        clue = []
        for x in range(len(args)/3):
            clue[x] = find_fake(str(arg[x*3]), str(arg[x*3+1]), str(arg[x*3+2]))

def new(args):
    lines = args
    coins = {}
    #seperate lines
#    if len(args) == 3:
#        lines.append(args)
#    for arg in range(int(len(args)/3+1)):
#        lines.append([args[arg*3], args[arg*3+1], args[arg*3+2]])
    print(lines)
    #this all assumes only one coin per line
    for line in lines:
        if line[2] == "left":
            coins[line[0]] = 1
            coins[line[1]] = 0
        elif line[2] == "right":
            coins[line[0]] = 0
            coins[line[1]] = 1
    print("Fake coins: ", end="")
    for x in coins:
        if not coins[x]:
            print(x, end=" ")
    print('\n')
            
if __name__ == "__main__":
    argv = argv[1:]
    args = []
    for x in range(int(len(argv)/3)):
        args.append((argv[x*3], argv[x*3+1], argv[x*3+2]))
        print(args)
    new(args)
