# Problem Set 1
# Name: Joshua Nelson
# Time spent: ~2 hours
# Comment: had to use example code as guideline.
#          Didn't think to use `while loan > 0 and current_months < months'

from ps1functions import *


def setBounds():
    stdin = input(
        "Are you dealing with small loans " +
        "or large (greater than one million) loans?\n" +
        "For an explanation of the difference in how the program acts, " +
        "type help. \n[default: small] ").lower()
    if stdin == "":
        stdin = 'small'
    if stdin == 'small':
        payment = 0
        delta = P/1000
    elif stdin == 'large':
        payment = P/12
        delta = P/1000
    elif stdin == 'help':
        print("This program works numberically, through trial and error. \n" +
              "    When the program receives the input 'small', " +
              "the first payment it tries is `principal/1000' " +
              "    and increments by the same amount. \n" +
              "    When it sees 'large', it tries `principle/12' " +
              "    to start and increments by `principal/1000'. \n" +
              "The latter method is much faster, but " +
              "inaccurate for small numbers.")
    else:
        print("This program only accepts 'small', " +
              "'large', and 'help' as arguments.")
        return setBounds()
    return payment, delta


P = get_principle()
apr = get_apr()
months = get_months()
payment = 0
interest = apr/12
loan = P
payment, delta = setBounds()

while loan > 0:
    payment += delta
    loan = P
    current_months = 0
    while loan > 0 and current_months < months:
        current_months += 1
        current_interest = interest * loan
        loan = loan - payment + current_interest

print(("Monthly payment necessary: {}\n" +
       "Number of months taken: {}\n" +
       "Total paid: {}\n" +
       "Amount paid to interest: {}").format(
    payment, current_months,
    current_months*payment, current_months*payment - P))
