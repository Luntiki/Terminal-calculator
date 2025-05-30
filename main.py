from math_operations import amount, difference, composition, division, degre, quotient, remainder

def two_numbers():
    first_number=input('Please write the first number:' )
    second_number=input('Please write the second number:' )

    try:
        if list(first_number).count('.') > 0 or list(second_number).count('.') > 0: 
            first_number = float(first_number)
            second_number = float(second_number)
        else:
            first_number = int(first_number)
            second_number = int(second_number)
    except ValueError:
        return('Error. Please write an intenger or decimal number')

    print('Possible actions: AMOUNT,  DIFFERENCE, COMPOSITION, DIVISION, DEGRE, QUOTIENT, REMAINDER')
    action=input('Pleace enter the action you want to perform on the numbers: ')

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

    if action_lower in operations:
        return(operations[action_lower](first_number, second_number))
    else:
        print('The operatin was not found. Check the correctness of the introduction')
print(two_numbers())