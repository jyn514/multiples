palindromes=[]
sequence=[]

def palindrome(x):
    for n in range (11, x):
        sequence = list(str(n))
        sequence.reverse()
        num=""
        for x in sequence:
            num+=str(x)
        if n == int(num):
            palindromes.append(n)
    print(palindromes)

palindrome(999999)
