



def palindrome(x):
    match=[]
    sequence=[]
    for n in range (x, 10, -1):
        sequence = list(str(n))
        sequence.reverse()
        num=""
        for x in sequence:
            num+=str(x)
        if n == int(num):
            match.append(n)
    greatest=match[0]
    print("Greatest palindrome is " + str(greatest))
    return greatest
    
def factor(n):
    factors=[]
    for x in range(2, int(n**.5)+1):
        if n%x == 0:
            factors.append(x)
    print("Factors:")
    print(factors)

greatest=palindrome(999999)
factor(greatest)
