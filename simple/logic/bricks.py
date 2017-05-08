def make_bricks(small, big, goal):
    while small >= 5:
        small -= 5
        big += 1
    if not goal % 5 and big >= goal / 5:
        return True
    else:
        mod = goal % 5
        if small < mod or big < goal / 5:
            return False
        else:
            return True

# http://codingbat.com/prob/p118406
