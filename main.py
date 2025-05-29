from math_operations import AMOUNT
from math_operations import DIFFERENCE
from math_operations import COMPOSITION
from math_operations import DIVISION


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

print('Possible actions: AMOUNT,  DIFFERENCE, COMPOSITION, DIVISION')
action=input('Pleace enter the action you want to perform on the numbers:')


if action == 'AMOUNT' or action == 'amount':
    print(AMOUNT(first_number, second_number))

if action == 'DIFFERENCE' or action == 'difference':
    print(DIFFERENCE(first_number, second_number))

if action == 'COMPOSITION' or action == 'composition':
    print(COMPOSITION(first_number, second_number))

if action == 'DIVISION' or action == 'division':
    print(DIVISION(first_number, second_number))