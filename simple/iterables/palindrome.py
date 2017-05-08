match = []


def palindrome(x):
    sequence = []
    for n in range(x, 10, -1):
        sequence = list(str(n))
        sequence.reverse()
        num = ""
        for x in sequence:
            num += str(x)
        if n == int(num):
            match.append(n)
    greatest = match[0]
    print("Greatest palindrome is " + str(greatest))
    return greatest


def factor(n):
    factors = []
    for x in range(2, int(n**.5) + 1):
        if n % x == 0:
            factors.append(x)
    return factors


greatest = palindrome(999999)
# change palindrome(x) to use a different limit
factor(greatest)

for x in match:
    for n in factor(x):
        if x / n < 1000:
            print(x, n)
