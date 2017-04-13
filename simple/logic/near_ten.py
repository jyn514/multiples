def near_ten(num):
    mod = num % 10
    if mod in [0, 1, 2, 8, 9]:
        return True
    else:
        return False
