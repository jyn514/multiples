sum = 0
L = [2]
a,b = 1, 2
while b<4000000:
    a,b = b, a+b
    if b%2 == 0:
        L.append(b)

for x in L:
    sum+=x

print(sum)
