#PROBLEM 2
from ps1functions import *
from find_months import find_months

def guess(guessx, principle, lower_bound, apr, upper_bound):
    return abs((guessx + find_months(principle, upper_bound, apr)) / 2)


principle = get_principle()
months = get_months()
apr = get_apr()
interest = apr/12
lower_bound = principle/12
upper_bound = (principle * ((1 + apr/12)**months))/12
print("{} {}".format(lower_bound, upper_bound))

guessx = (lower_bound + upper_bound)
x=0
temp = find_months(principle, guessx, apr)
while abs(temp  - find_months(principle, temp, apr)) >= 10:
    guessx = guess(guessx, principle, lower_bound, apr, upper_bound)
    x+=1
    temp = find_months.main(principle, guessx, apr)
print(x + guessx)
