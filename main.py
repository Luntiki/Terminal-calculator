from math_operations import AMOUNT, DIFFERENCE, COMPOSITION, DIVISION, DEGRE, QUOTIENT, REMAINDER

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
    print('Error. Please write an intenger or decimal number')

print('Possible actions: AMOUNT,  DIFFERENCE, COMPOSITION, DIVISION, DEGRE, QUOTIENT, REMAINDER')
action=input('Pleace enter the action you want to perform on the numbers:')

operations={
    'amount': AMOUNT,
    'difference': DIFFERENCE,
    'composiotion': COMPOSITION,
    'division': DIVISION,
    'degre': DEGRE,
    'quotient': QUOTIENT,
    'remainder': REMAINDER,
}
action_lower=action.lower() 
if action_lower in operations:
    print(operations[action_lower](first_number, second_number))
else:
    print('The operatin was not found. Check the correctness of the introduction')