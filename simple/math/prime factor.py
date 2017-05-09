from sys import argv


def prime_factor(n):
    primes = set()
    for x in range(2, int(n / 2) + 1):
    # less than half the number and smaller than two
        if not n % x:
        # x is a factor
            if all(x % y != 0 for y in range(2, int(x / 2) + 1)):
            # x can't be divided evenly
                primes.add(x)
    if not primes:  # n is prime
        primes = [n]
    return primes


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
