def love6(a, b):
    if a == 6 or b == 6:
        return True
    else:
        return abs(b - a) == 6 or b + a == 6
