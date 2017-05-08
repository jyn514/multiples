def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def simplify(a, b):
    div = gcd(a, b)
    return int(a / div), int(b / div)
