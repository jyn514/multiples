principle = 5000
apr = .18
payment_rate = .02
months = 0
while principle>0:
    interest, payment = principle * apr / 12, principle * payment_rate
    principle = principle + interest - payment
    months += 1
    print(str(principle) + " " + str(months))
print(months)
