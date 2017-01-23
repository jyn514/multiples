def prime_factor(n):
    primes=[]
    for x in range(2, int(n/2)+1):
      if not n%x:
        if all(x%y != 0 for y in range(2, x)):
            primes.append(x)
    return primes 
