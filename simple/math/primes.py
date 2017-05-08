class prime:
    def is_prime(num):
        if all(num % y != 0 for y in range(2, num)):
            return True
        else:
            return False

    def next(num):
        num += 1
        while not (prime.is_prime(num)):
            num += 1
        return num

    def previous(num):
        num -= 1
        while not (prime.is_prime(num)):
            num -= 1
        return num

    def all_below(num):
        for x in range(2, num):
            if prime.is_prime(x):
                print(x, end=" ")
