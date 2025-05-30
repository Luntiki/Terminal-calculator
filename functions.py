from math_operations import amount, difference, composition, division, degre, quotient, remainder, comb, perm
from math_operations import factorial

def one_number():
    number_one=input("Please write the number: ")
    try:
        if list(number_one).count('.') == 1:
            number_one=float(number_one)
        else:
            number_one=int(number_one)
    except ValueError:
        return('Error. Please write an intenger or decimal number')
    def choosing_an_action(number_one):
        print("Possible actions: factorial")
        action=(input("Please enter the action you want to perform on the numbers: "))
        operations={
            'factorial': factorial,
        }
        action_lower=action.lower()
        try:
            return operations[action_lower](number_one)
        except KeyError:
            print('The operatin was not found. Check the correctness of the introduction')
            choosing_an_action()


def two_numbers():
    first_number=input('Please write the first number: ')
    second_number=input('Please write the second number: ')
    try:
        if list(first_number).count('.') == 1 or list(second_number).count('.') == 1: 
            first_number, second_number = float(first_number), float(second_number)
        else:
            first_number, second_number = int(first_number), int(second_number)
    except ValueError:
        return('Error. Please write an intenger or decimal number')

    def choosing_an_action(first_number, second_number):
        print('Possible actions: AMOUNT,  DIFFERENCE, COMPOSITION, DIVISION, DEGRE, QUOTIENT, REMAINDER')
        action=input('Please enter the action you want to perform on the numbers: ')
        operations={
            'amount': amount,
            'difference': difference,
            'composiotion': composition,
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
