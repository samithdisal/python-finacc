__author__ = 'samiths'

from math import pow, e


def annual_percentage_yield(r, n):
    return pow(1+(r/n), n)-1


def balloon_loan_payment(pv, bamt, r, n):
    return (pv-(bamt/pow(1+r, n)))*(r/(1-pow(1+r, n*-1)))


def compound_interest(p, r, n):
    return p*(pow(1+r, n)-1)


def continuous_compounding(p, r, t):
    return p*pow(e, r*t)


def dept_to_income_ratio(debt, income):
    return debt/income


print compound_interest(1000, .10, 12)