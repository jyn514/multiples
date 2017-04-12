months = 0
principle = 0
payment = 0
apr = 0

def apr_in():
    stdin = input("Enter annual interest as a percent or positive decimal [default .18]: ")
    if stdin == "":
        apr = .18
    elif float(stdin) >= 1:
        apr = float(stdin)/100
    elif float(apr) <= 0:
       raise ValueError
    else:
        apr = float(stdin5)
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
#future update: allow format [yearly payment/12]

def principle_in():
    stdin = (input("Enter principle of loan "
                        "as a positive number [default 5000]: "))
    if stdin == "":
        principle = 5000
    elif float(stdin) <= 0:
        principle = 5000
    else:
        principle = float(stdin)
    return principle

while not apr:
    try:
        apr = apr_in()
    except ValueError:
        print("Value error. Remember that apr must be a percent or positive decimal. "
              "If you typed a percent, please do not include a percent sign. ")
print("APR is {}".format(apr))

while not payment:
    try:
        payment = payment_in()
        if payment <= 0:
            payment = 100
    except ValueError:
        print("Value error. You probably made a typo.")
print("Monthly payment is {}".format(payment))

while not principle:
    try:
        principle = principle_in()
    except ValueError:
        print("Value error. You probably made a typo. ")
print("Principle is {}. ".format(principle))

if apr/12 > payment:
    print("The montly payment is less than the starting increase in interest. "
            "This loan will never be paid off because all payment will go to interest, not principle. ")

while principle>0:
    interest = principle * (apr / 12)
    principle = principle + interest - payment
    months += 1
    if principle < 0:
        break
    print(str(principle) + " " + str(months))
print("It would take {} months to pay off the loan with the given parameters.".format(months))

