def alarm_clock(day, vacation):
    if day > 0 and day < 6:
        if vacation:
            return "10:00"
        else:
            return "7:00"
    else:
        if vacation:
            return "off"
        else:
            return "10:00"
