def factor(n):
    factors = []
    for x in range(2, int(n**.5) + 1):
        if n % x == 0:
            factors.append(x)
    return factors


def prime_factor(n):
    primes = []
    for x in range(2, int(n / 2) + 1):
        if not n % x:
            if all(x % y != 0 for y in range(2, x)):
                primes.append(x)
    return primes


def find_divisible(x, y):
    factor_guess = list(range(x, y + 1))
    factor_necc = []
    for g in factor_guess:
        if factor_necc == []:
            factor_necc.append(g)
        else:
            for n in factor_necc:
                if not g % n:
                    factor_necc.append(g)
    print(factor_necc)
    product = 1
    for x in range(x, y + 1):
        product *= x
    print(product)
    factors = factor(product)
    for f in factors:
        if f > y:
            factors.remove(f)
    print(sorted(set(factors)))
