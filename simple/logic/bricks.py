def make_bricks(small, big, goal):
    if not goal % 5 and big >= goal / 5:
        return True
    mod = goal % 5
    if small < mod or (big < goal / 5 and small < 5) or small + big * 5 < goal:
        return False
    return True
