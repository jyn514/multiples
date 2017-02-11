from random import randint
def cointoss(n):
    tries=0
    heads=0
    tails=0
    while tries<n:
        if randint(0,1)==1:
            heads+=1
        else:
            tails+=1
        tries+=1
    print("Number of heads: ", heads)
    print("Number of tails: ", tails)
