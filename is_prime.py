def is_prime(num):
    num = abs(num)
    if num in [0, 1, 2]:
#corner cases
        if num == 2:
            return True
        else:
            return False
    elif all(num%y != 0 for y in range(2, num)):
          return True
    else:
        return False
