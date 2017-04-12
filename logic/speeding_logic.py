def caught_speeding(speed, is_birthday):
    if speed <= 85:
        if is_birthday:
            return int(not speed <= 65)
        elif (speed > 60 and speed <= 80):
            return 1
        elif speed > 80:
            return 2
        else:
            return 0
    else:
        return 2
