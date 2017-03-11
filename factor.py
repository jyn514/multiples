def divisors(integer):
    factors=[]
    if integer == 2 or integer == 3:
        return [integer]
    elif integer == 1 or integer == 0:
        return []
    for x in range(2, int(integer/2)+1):
        if not integer%x:
            factors.append(x)
    if factors==[]:
        return [integer]
    else:
        return factors

def prime_factors(x):
    if type(x) == int:
        factors = divisors(x)
    for n in factors:
        while divisors(n) != [n]:
            temp = divisors(n)
            if temp != []:
                factors += temp
    return factors
