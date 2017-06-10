from sys import argv


def prime_factors(n):
"""Credit to this forum: https://stackoverflow.com/a/22808285"""
    i = 2
    # factor to test
    factors = []
    while i * i <= n:
    # `i` can't be prime unless less than sqrt(n)
        if n % i:
        # not a factor
            i += 1
        else:
            n //= i
            print(i)
    if n > 1:
        print(n)
    return factors


def prime_tree(n):
    primes = prime_factor(n)
    tree = {}    
    for x in primes:
        new = n / x           # first iteration doesn't need loop
        tree[x] = 1           # initialize the key
        while not (new % x):  # x is a factor of new
            tree[x] += 1
            new /= x
    return tree

if __name__ == "__main__":
    try:
        integer = int(argv[1])
    except (ValueError, IndexError):
        integer = 400000
        print("Using sample value 400,000")
        print("This is the same as (2 ** 7) * (5 ** 5)")
    print("Factors | Power")
    tree = prime_tree(integer)
    for key, value in tree.items():
        print(str(key).center(10), value)
