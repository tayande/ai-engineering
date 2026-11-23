# 1. Factorial (needed for Poisson)
"""
k! means 1 × 2 × … × k. It uses the running-total pattern you know, but multiplying instead of adding:
"""
import math

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

"""
result starts at 1, not 0, because multiplying by 0 would wipe everything out. That also makes factorial(0) = 1 automatically, which is correct.
"""

# 2. The distributions as functions
# Each one is the formula from Step 2, written in Python:
def bernoulli_pmf(k, p):
    if k == 1:
        return p
    return 1 - p

def poisson_pmf(k, lam):
    return (lam ** k) * math.exp(-lam) / factorial(k)

def normal_pdf(x, mu, sigma):
    coeff = 1 / (sigma * math.sqrt(2 * math.pi))
    return coeff * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

"""
math.exp(x) means e^x.
lam is used instead of lambda because lambda is a reserved word in Python.
"""

# 
