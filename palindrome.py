palindromes=[]

def palindrome(x):
    for n in range (11, x):
        if int(string(list(sort(list(string(x))), reversed = true))) == x:
            palindromes.append(x)
            
