from sys import argv


def divisors(integer):
    factors = []
    if integer in [0, 1, 2, 3]:    #corner cases
        return factors
    else:
        for x in range(2, int(integer / 2) + 1):
            if not integer % x:
                factors.append(x)
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


if __name__ == "__main__":
    try:
        integer = int(argv[1])
    except (ValueError, IndexError):
        integer = 400000
    print("Factors of {}:".format(integer))
    for x in divisors(integer):
        print(x, end=" ")
    print()
