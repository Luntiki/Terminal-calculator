from math_operations import amount, difference, composition, division, degre, quotient, remainder

def two_numbers():
    first_number=input('Please write the first number: ')
    second_number=input('Please write the second number: ')
    try:
        if list(first_number).count('.') > 0 or list(second_number).count('.') > 0: 
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
        }
        action_lower=action.lower() 
        try:
            return operations[action_lower](first_number, second_number)
        except KeyError:
            print('The operatin was not found. Check the correctness of the introduction')
            choosing_an_action(first_number, second_number)

    return choosing_an_action(first_number, second_number)

print(two_numbers())