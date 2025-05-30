# basic python mathematical operaions 
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
