def AMOUNT(first_number, second_number):
    return first_number + second_number

def DIFFERENCE(first_number, second_number):
    return first_number - second_number

def COMPOSITION(first_number, second_number):
    return first_number * second_number

def DIVISION(first_number, second_number):
    if second_number != 0:
        return first_number / second_number
    else:
        return 'Error. In cannot be divided by 0'
