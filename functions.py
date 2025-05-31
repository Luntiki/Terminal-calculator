from math_operations import amount, difference, composition, division, degre, quotient, remainder, comb, perm, copysign, isclose, dist
from math_operations import factorial, isqrt, ceil, fabs, floor, modf, trunc, frexp, ldexp, ulp, cbrt, exp, exp2, expm1, log, log1p, log2, degress, radians, acos, asin, atan, cos, sin, tan, acosh, asinh, atanh, cosh, sinh, tanh, erf, erfc, gamma, lgamma
from math_operations import average_value

def one_number():
    number_one=input("Please write the number: ")
    try:
        if list(number_one).count('.') == 1:
            number_one=float(number_one)
        else:
            number_one=int(number_one)
    except ValueError:
        print('Error. Please write an intenger or decimal number')
        return one_number()
    def choosing_an_action(number_one):
        print("Possible actions: factorial, actorial, isqrt, ceil, fabs, floor, modf, trunc, frexp, ldexp, ulp, cbrt, exp, exp2, expm1, log, log1p, log2, degress, radians, acos, asin, atan, cos, sin, tan, acosh, asinh, atanh, cosh, sinh, tanh, erf, erfc, gamma, lgamma")
        action=(input("Please enter the action you want to perform on the number: "))
        operations={
            'factorial': factorial,
            'isqrt': isqrt,
            'ceil': ceil,
            'fabs': fabs,
            'floor': floor,
            'modf': modf,
            'trunc': trunc,
            'frexp': frexp,
            'ldexp': ldexp,
            'ulp': ulp,
            'cbrt': cbrt,
            'exp': exp,
            'exp2': exp2,
            'expm1': expm1,
            'log': log,
            'log1p': log1p,
            'log2': log2,
            'degress': degress,
            'radians': radians,
            'acos': acos,
            'asin': asin,
            'atan': atan,
            'cos': cos,
            'sin': sin,
            'tan': tan,
            'acosh': acosh,
            'asinh': asinh,
            'atanh': atanh,
            'cosh': cosh,
            'sinh': sinh,
            'tanh': tanh,
            'erf': erf,
            'erfc': erfc,
            'gamma': gamma,
            'lgamma': lgamma,
        }
        action_lower=action.lower()
        try:
            return operations[action_lower](number_one)
        except KeyError:
            print('The operatin was not found. Check the correctness of the introduction')
    return choosing_an_action(number_one)



def two_numbers():
    first_number=input('Please write the first number: ')
    second_number=input('Please write the second number: ')
    try:
        if list(first_number).count('.') == 1 or list(second_number).count('.') == 1: 
            first_number, second_number = float(first_number), float(second_number)
        else:
            first_number, second_number = int(first_number), int(second_number)
    except ValueError:
        print('Error. Please write an intenger or decimal number')
        return two_numbers()
    def choosing_an_action(first_number, second_number):
        print('Possible actions: amount,  difference, composition, division, degre, quotient, remainder, comb, perm, copysign, isclose, dist')
        action=input('Please enter the action you want to perform on the numbers: ')
        operations={
            'amount': amount,
            'difference': difference,
            'composition': composition,
            'division': division,
            'degre': degre,
            'quotient': quotient,
            'remainder': remainder,
            'comb': comb,
            'perm': perm,
            'copysign': copysign,
            'isclose': isclose,
            'dist': dist,
        }
        action_lower=action.lower() 
        try:
            return operations[action_lower](first_number, second_number)
        except KeyError:
            print('The operatin was not found. Check the correctness of the introduction')
            choosing_an_action(first_number, second_number)

    return choosing_an_action(first_number, second_number)



def set_of_numbers():
    try:
        value=int(input("Please enter the number of values: "))
    except ValueError:
        print('Error. Please write an intenger number')
        return set_of_numbers()
    son=list() #set of naumbers
    for i in range(value):
        son.append(float(input("Please enter the number: ")))
    def choosing_an_action(son):
        operations={
            'average value': average_value,
        }
        print("Possible actions: average value")
        action=input("Please enter the action: ")
        action_lower=action.lower()
        try:
            return operations[action_lower](son)
        except KeyError:
            print("The operatin was not found. Check the correctness of the introduction")
            return choosing_an_action(son)
    return choosing_an_action(son)