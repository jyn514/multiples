#PROBLEM 1

def months_in():
    stdin = input("Enter the time, in months, in which you wish to pay off your loan [default 120]: ")
    if stdin == "":
        return 120
    elif float(stdin) == 0:
        print("This input doesn't make sense. If you take out a loan, you don't repay it immediately. Please enter something else.")
    elif float(stdin) < 0:
        print("This input doesn't make sense. You can't pay a loan in negative time. Please enter something else.")
    else:
        return float(stdin)

def get_months():
    months = 0
    while not months:
        try:
            months = months_in()
        except ValueError:
            print("Value error.")
    print("You have selected {} months. ".format(months))
    return months

def apr_in():
    stdin = input("Enter annual interest as a percent or positive decimal [default .18]: ")
    if stdin == "":
        apr = .18
    elif float(stdin) >= 1:
        apr = float(stdin)/100
    elif float(stdin) <= 0:
       raise ValueError
    else:
        apr = float(stdin)
    return apr

def get_apr():
    apr = 0
    while not apr:
        try:
            apr = apr_in()
        except ValueError:
            print("Value error. Remember that apr must be a percent or positive decimal. "
                  "If you typed a percent, please do not include a percent sign. ")
    print("APR is {}".format(apr))
    return apr

def payment_in():
    stdin = input("Enter monthly payment as a dollar amount [default 100]: ")
    if stdin == "":
        payment = 100
    elif float(stdin) <= 0:
        raise ValueError
    else:
        payment = float(stdin)
    return payment
#future update: allow format "yearly payment/12"

def get_payment():
    payment = 0
    while not payment:
        try:
            payment = payment_in()
            if payment <= 0:
                payment = 100
        except ValueError:
            print("Value error. You probably made a typo.")
    print("Monthly payment is {}".format(payment))
    return payment

def principle_in():
    stdin = input("Enter principle of loan as a positive number [default 5000]: ")
    if stdin == "":
        principle = 5000
    elif float(stdin) <= 0:
        principle = 5000
    else:
        principle = float(stdin)
    return principle

def get_principle():
    principle = 0
    while not principle:
        try:
            principle = principle_in()
        except ValueError:
            print("Value error. You probably made a typo. ")
    print("Principle is {}. ".format(principle))
    return principle
