def squirrel_play(temp, is_summer):
    if temp >= 60:
        if is_summer:
            return temp <=100
        else:
            return temp <= 90
    else:
        return False
