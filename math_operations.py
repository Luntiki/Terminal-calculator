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
