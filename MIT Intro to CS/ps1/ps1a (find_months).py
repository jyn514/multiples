#Problem Set 1
#Name: Joshua Nelson
#Time: ~20 minutes
from ps1functions import *

P = get_principle()
apr = get_apr()
payment = get_payment()
def find_months(principle, payment, apr):
    if apr/12 > payment:
        print("The montly payment is less than the starting increase in interest. "
                "This loan will never be paid off because all payment will go to interest, not principle. ")
    months = 0
    while principle>0:
        interest = principle * (apr / 12)
        principle = principle + interest - payment
        months += 1
        if principle < 0:
            break
        print(str(principle) + " " + str(months))
    print("It would take {} months to pay off the loan with the given parameters.".format(months))
    return months
find_months(P, payment, apr)
