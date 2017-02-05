def divisors(integer):
    factors=[]
    for x in range(2, int(integer/2)+1):
        if not integer%x:
            factors.append(x)
    if factors==[]:
        return str(integer) + " is prime"
    else:
        return factors
