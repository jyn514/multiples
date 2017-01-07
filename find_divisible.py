def divisible(n, x, y):
    match = []
    for a in range(x, y+1):
        if n%a == 0:
            match.append(a)
    if match==list(range(x, y+1)):
        print("match")
        return "match"
    else:
        print("no match")

def factor(n):
    factors=[]
    for x in range(2, int(n**.5)+1):
        if n%x == 0:
            factors.append(x)
    return factors

def find_divisible(x, y):
    product = 1
    for x in range(x, y+1):
        product*=x
    print(product)
    if divisible(product, x, y) == "match":
        factors = set(factor(product))
        print (sorted(factors))
    else:
        print("error")
