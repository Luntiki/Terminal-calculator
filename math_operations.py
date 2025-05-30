import math

# module math
## 2 numbers

def comb(first_number, second_number):
    return math.comb(first_number, second_number)

def perm(first_number, second_number):
    return math.perm(first_number, second_number)

def copysign(first_number, second_number):
    return math.copysign(first_number, second_number)

def isclose(first_number, second_number):
    rel_tol=float(abs(input("Enter the relative error: ")))
    abs_tol=float(abs(input("Enter the absolute tolerance: ")))
    return math.isclose(first_number, second_number, rel_tol, abs_tol)

def dist(first_number, second_number):
    return math.dist(first_number, second_number)

## 1 numbers

def factorial(number_one):
    return math.factorial(number_one)

def isqrt(number_one):
    return math.isqrt(number_one)

def ceil(number_one):
    return math.ceil(number_one)

def fabs(number_one):
    return math.fabs(number_one)

def floor(number_one):
    return math.floor(number_one)

def modf(number_one):
    return math.modf(number_one)

def trunc(number_one):
    return math.trunc(number_one)

def frexp(number_one):
    return math.frexp(number_one)

def ldexp(number_one):
    return math.ldexp(number_one)

def ulp(number_one):
    return math.ulp(number_one)

def cbrt(number_one):
    return math.cbrt(number_one)

def exp(number_one):
    return math.exp(number_one)

def exp2(number_one):
    return math.exp2(number_one)

def expm1(number_one):
    return math.expm1(number_one)

def log(number_one):
    return math.log(number_one)

def log1p(number_one):
    return math.log1p(number_one)

def log2(number_one):
    return math.log10(number_one)

def degress(number_one)
    return math.degrees(number_one)

def radians(number_one)number_one:
    return math.radians(number_one)

def acos(number_one):
    return math.acos(number_one)

def asin(number_one):
    return math.asin(number_one)

def atan(number_one):
    return math.atan(number_one)

def cos(number_one):
    return math.cos(number_one)

def sin(number_one):
    return math.sin(number_one)

def tan(number_one):
    return math.tan(number_one)

def acosh(number_one):
    return math.acosh(number_one)

def asinh(number_one):
    return math.asinh(number_one)

def atanh(number_one):
    return math.atanh(number_one)

def cosh(number_one):
    return math.cosh(number_one)

def sinh(number_one):
    return math.sinh(number_one)

def tanh(number_one):
    return math.tanh(number_one)

def erf(number_one):
    return math.erf(number_one)

def erfc(number_one):
    return math.erfc(number_one)

def gamma(number_one):
    return math.gamma(number_one)
number_one
def lgamma(number_one):
    return math.lgamma(number_one)


# basic python mathematical operaions 
## 2 numbers

def amount(first_number, second_number):
    return first_number + second_number

def difference(first_number, second_number):
    return first_number - second_number

def composition(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    if second_number != 0:
        return first_number / second_number
    else:
        return 'Error. In cannot be divided by 0'

def degre(first_number, second_number):
    return first_number ** second_number

def quotient(first_number, second_number):
    return first_number // second_number

def remainder(first_number, second_number):
    return first_number % second_number
