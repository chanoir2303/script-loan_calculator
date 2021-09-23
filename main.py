import argparse
import math

# define arguments
parser = argparse.ArgumentParser()
parser.add_argument('--type',
                    choices=['annuity', 'diff'])
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--payment')
parser.add_argument('--interest')
args = parser.parse_args()

# define global total to use it in loop
total = 0

# for 'diff' as --type
if args.type == 'diff' and args.interest:

    # calculate rate from interest argument
    rate_interest = float(args.interest) * 0.01 / 12

    for i in range(1, int(args.periods) + 1):
        # calculate diff payment
        diff_payment = math.ceil(float(args.principal) / float(args.periods) + rate_interest * (
                    float(args.principal) - (float(args.principal) * (i - 1) / float(args.periods))))

        # add each iteration to calculate total at the end of the loop
        total = total + diff_payment

        print('Month ' + str(i) + ': ' + 'payment is ' + str(diff_payment))

    # calculate overpayment
    overpayment = total - int(args.principal)
    print(f'Overpayment = {overpayment}')

# for 'annuity' as --type
elif args.type == 'annuity' and args.interest:

    # calculate rate from interest argument
    rate_interest = float(args.interest) * 0.01 / 12

    # calculate annuity payment
    if args.principal and args.periods:
        annuity_payment = math.ceil(
            (float(args.principal)) * (rate_interest * math.pow(1 + rate_interest, float(args.periods)))
            /
            (math.pow(1 + rate_interest, float(args.periods)) - 1))

        # calculate overpayment
        overpayment = (annuity_payment * int(args.periods)) - int(args.principal)

        print('Your annuity payment = ' + str(annuity_payment) + '!')
        print(f'Overpayment = {overpayment}')

    # calculate loan principal
    elif args.payment and args.periods:
        principal = math.floor(float(args.payment)
                   /
                   ((rate_interest * (math.pow(1 + rate_interest, float(args.periods))))
                    /
                    (math.pow(1 + rate_interest, float(args.periods)) - 1)))

        # calculate overpayment
        overpayment = (int(args.payment) * int(args.periods)) - principal

        print('Your loan principal = ' + str(principal) + '!')
        print(f'Overpayment = {overpayment}')

    # calculate periods
    elif args.principal and args.payment:
        nbr_monthly_payment = float(args.payment) / (float(args.payment) - (rate_interest * float(args.principal)))
        result = math.ceil(math.log(nbr_monthly_payment, 1 + rate_interest))

        # convert result to how many years and months
        years = math.floor(result / 12)

        # calculate overpayment
        overpayment = result * int(args.payment) - int(args.principal)

        print(f'It will take {years} years to repay this loan!')
        print(f'Overpayment = {overpayment}')
else:
    print('Incorrect parameters.')
