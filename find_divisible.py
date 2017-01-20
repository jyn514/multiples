def prime(x):
    remainders = []
    if (x == 2):
        return 1
    for y in range(2, x-1):
        remainders.append(bool (x%y))
    if all(remainders):
        return 1
    else:
        return 0

def factor(n):
    factors = []
    for x in range(2, int(n/2)+1):
        if n%x == 0:
            factors.append(x)
    return factors

def prime_factor(n):
    primes=[]
    for x in factor(n):
        if (prime(x)):
            primes.append(x)
    return primes

def find_divisible(x, y):
    product = 1
    for x in range(x, y+1):
        product*=x
    print(product)
    primes=[]
    while product > 1:
        for x in prime_factor(product):
            primes.append(x)
        print(primes)
        for x in primes:
            if product % x == 0:
                product /= x
        print(product)
    composites = list(range(x, y+1))
    for x in primes:
        try:
            composites.remove(x)
        except: pass
    print("Composites: " + str(composites))
    repeats = []
    for x in composites:
        for y in primes:
            if x%y == 0:
                x/=y
                break
        repeats.extend(prime_factor(x))
//currently only works for perfect squares, who knows why
        print(repeats)

find_divisible(1, 10)
