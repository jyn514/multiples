def divisible(n, x, y):
    match = []
    for a in range(x, y+1):
        if n%a==0:
            match.append(a)
    if match==list(range(x, y+1)):
        print("match")
    else:
        print("no match")
    
