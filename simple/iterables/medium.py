def double_char(str):
    new = []
    for char in str:
        new.append(2 * char)
    return "".join(new)


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a == b[-len(a):] or b == a[-len(b):]
# but the easy way was b.endswith(a[0])


def make_bricks(small, big, goal):
    if small + big * 5 < goal:
        return False
    elif (big < goal // 5) and (small < goal % 5):
        return False
    elif small < goal % 5:
        return False
    else:
        return True


def lone_sum(*arg):
    List = []
    for i in arg:
        List.append(i)
    sum = 0
    L = List[:]
    for x in L:
        I = L.pop(0)
        if I in L:
            while I in List:
                List.remove(I)
    for i in List:
        sum += i
    return sum
# inefficient, want to clean this up


def lucky_sum(*args):
    sum = 0
    for x in args:
        if x == 13:
            return sum
        else:
            sum += x
    return sum


def no_teen_sum(*args):
    sum = 0
    for x in args:
        if x not in [13, 14, 17, 18, 19]:
            sum += x
    return sum


def round_sum(*args):
    sum = 0
    for x in args:
        sum += round(x, -1)
    return int(sum)


def make_chocolate(small, big, goal):
    if (small + big * 5 < goal or
            small < goal % 5 or
            (big < goal // 5 and small < goal % 5)):
        return -1
    else:
        big_used = min(goal // 5, big)
        return goal - 5 * big_used


def close_far(a, b, c):
    if abs(a - b) <= 1 and abs(c - b) >= 2 and abs(c - a) >= 2:
        return True
    elif abs(a - c) <= 1 and abs(b - c) >= 2 and abs(b - a) >= 2:
        return True
    else:
        return False
