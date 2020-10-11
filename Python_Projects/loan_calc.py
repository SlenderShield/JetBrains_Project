# import math
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--type', required=True, help="")
# parser.add_argument('--principal')
# parser.add_argument('--payment')
# parser.add_argument('--periods')
# parser.add_argument('--interest')
# args = parser.parse_args()
#
#
# def argument(args):
# 	if args.type == 'annuity':
# 		pass
# 	elif args.type == 'diff':
# 		pass
#
#
# def m_type(principal):  # used to find the number of months for payments
# 	mon_pay = int(input("Enter the monthly payment: \n"))  # monthly pay
# 	interest = float(input("Enter the loan interest: \n"))  # interest for loan
# 	inter = (interest / (12 * 100))  # nominal rate for the loan
# 	value = (mon_pay / (mon_pay - inter * principal))  # finding the special value
# 	return math.ceil(math.log(value, (1 + inter)))  # return the no of months required
#
#
# def parity(user_type):
# 	if user_type == 'p':
# 		annual_pay = float(input("Enter the annuity payment: \n"))  # taking annual  payment
# 	else:
# 		principal = int(input("Enter the loan principal: \n"))  # taking principal amount
# 	months = int(input("Enter the number of periods: \n"))  # monthly pay
# 	interest = float(input("Enter the loan interest: "))  # interest for loan
# 	nominal_int = (interest / (12 * 100))  # nominal rate for the loan
# 	value = math.pow(1 + nominal_int, months)  # finding the special value
# 	denominator = (nominal_int * value / (value - 1))
# 	if user_type == 'p':
# 		return math.ceil(annual_pay / denominator)
# 	else:
# 		return math.ceil(principal * denominator)
#
#
# print("""What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal: """)
# user_type = input()
#
# if user_type == 'n':
# 	principal = int(input("Enter the loan principal: \n"))
# 	months = m_type(principal)
# 	if months == 1:
# 		print(f"It will take {months} month to repay the loan")
# 	else:
# 		years = months // 12
# 		month = months % 12
# 		print(f"It will take {years} years and {month} months to repay this loan!")
# elif user_type == 'p':
# 	principal = parity(user_type)
# 	print(f"Your loan principal = {principal}!")
# elif user_type == 'a':
# 	monthly_pay = parity(user_type)
# 	print(f"Your monthly payment = {monthly_pay}!")
# else:
# 	exit()


import argparse
import math

"""
Stage 4/4
"""
pay_type = None     # Type of payments: "annuity" or "diff" (differentiated)
a = None            # annuity/payment
p = None            # principal
n = None            # number of months / number of periods
i = None            # interest rate


def parse_args(args):
    global pay_type
    global a
    global p
    global n
    global i

    if args.principal and args.principal >= 0:  # had to ad 'and args.principal' to make the check work, if you just run the code in the terminal it works without 'and args.principal', just need 'args.principal >= 0
        p = args.principal
    if args.periods and args.periods >= 0:
        n = args.periods

    if args.interest and args.interest >= 0.0:
        i = args.interest

        if args.type:
            pay_type = args.type

            if args.type == 'annuity':
                if args.payment and args.payment >= 0:
                    a = args.payment
                if (p is None and n is None) or \
                        (n is None and a is None) or \
                        (a is None and p is None):
                    return False
                return True

            elif args.type == 'diff':
                if args.payment:
                    return False
                elif p is not None and n is not None:
                    return True
    return False


def interest_rate():
    interest = i * 0.01 / 12
    return interest


def annuity_payment():
    interest = interest_rate()
    annuity = math.ceil(p * ((interest * math.pow(1 + interest, n)) / ((math.pow(1 + interest, n)) - 1)))
    overpay = annuity * n - p
    print('Your annuity payment = {}!\nOverpayment = {}'.format(math.ceil(annuity), math.ceil(overpay)))


def loan_principal():
    interest = interest_rate()
    loan_p = a / ((interest * math.pow(1 + interest, n)) / (math.pow(1 + interest, n) - 1))
    overpay = a * n - math.floor(loan_p)
    print('Your loan principal = {}! \nOverpayment = {}'.format(math.ceil(loan_p), math.ceil(overpay)))


def number_of_payments():    # convert months to year(s) and months
    interest = interest_rate()
    periods = math.ceil(math.log(a / (a - interest * p), (1 + interest)))
    y, m = divmod(periods, 12)
    year_str = 'year'
    month_str = 'month'
    if y > 1:
        year_str += 's'
    if m > 1:
        month_str += 's'
    if m > 0:
        print('It will take {} {} and {} {} to repay this loan!'.format(y, year_str, m, month_str))
    else:
        print('It will take {} {} to repay this loan!'.format(y, year_str))
    overpay = a * periods - p
    print('Overpayment = {}'.format(math.ceil(overpay)))


def differentiated_payment():     # n = periods (number of months), principal = p, i = interest rate
    interest = interest_rate()
    total = 0
    for m in range(1, n + 1):                # m = from 1 to n
        d_m = math.ceil(p / n + interest * (p - ((p * (m - 1)) / n)))
        total += d_m
        print('Month {}: paid out {}'.format(m, d_m))
    overpay = total - p
    print('Overpayment = {}'.format(math.ceil(overpay)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', help='Type of payment: "annuity" or "diff" (differentiated)')
    parser.add_argument('--payment', help='Monthly payment', type=int)
    parser.add_argument('--principal', help='To calculate payment', type=int)
    parser.add_argument('--periods', help='The number of months and/or years needed to repay the credit', type=int)
    parser.add_argument('--interest', help='Is specified without a percent sign', type=float)

    if parse_args(parser.parse_args()):
        if pay_type == 'annuity':
            if a is None:
                annuity_payment()
            elif p is None:
                loan_principal()
            elif n is None:
                number_of_payments()
        elif pay_type == 'diff':
            differentiated_payment()
    else:
        print('Incorrect parameters')


main()
