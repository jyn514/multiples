#Problem Set 1
#Name: Joshua
#Time: ~20 minutes

from ps1functions import *

P = get_principle()
apr = get_apr()
months = get_months()
min_payment, max_payment, loan = 0, P, P
interest = apr/12
payment = (min_payment + max_payment) / 2

while abs(loan) > 10:
    current_months, loan = 0, P
    payment = (min_payment + max_payment) / 2
    while current_months < months:
        current_months += 1
        current_interest = interest * loan
        loan = loan - payment + current_interest
    if loan > 0: #not paying enough
        min_payment = payment
    elif loan < 0: #paying too much
        max_payment = payment
        
print("Monthly payment necessary: {}\nNumber of months taken: {}\nTotal paid: {}\nAmount paid to interest: {}".format(payment, current_months, current_months*payment, current_months*payment - P))
