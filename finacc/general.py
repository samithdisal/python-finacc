__author__ = 'samiths'

from math import pow, e, log as ln, log10


def annuity_future_value(p, r, n):
    return p*((pow(1+r, n)-1)/r)


def annuity_fv_continuous_compounding(cf, r, t):
    return cf*((pow(e, r*t)-1)/(pow(e, r)-1))


def annuity_present_value(p, r, n):
    return p*((1-pow(1+r, n*-1))/r)


def annuity_fv_solve_for_n(fv, p, r):
    return ln(1+((fv*r)/p))/ln(1+r)


def annuity_pv_solve_for_n(pv, p, r):
    return ln(pow(1-((pv*r)/p), -1))/ln(1+r)


def annuity_payment_pv(pv, r, n):
    return (r*pv)/(1-pow(1+r, n*-1))


def annuity_payment_fv(fv, r, n):
    return (fv*r)/(pow(1+r, n)-1)


def annuity_pv_factor(r, n):
    return (1-pow(1+r, n*-1))/r


def annuity_due_payment_fv(fv, r, n):
    return fv*(r/(pow(1+r, n)-1))*(1/(1+r))


def annuity_due_payment_pv(pv, r, n):
    return pv*(r/(1-pow(1+r, n*-1)))*(1/(1+r))


def doubling_time(r):
    return log10(2)/(log10(1+r))


def doubling_time_continues_compounding(r):
    return ln(2)/r


