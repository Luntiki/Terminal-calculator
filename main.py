from functions import one_number, two_numbers, set_of_numbers

while True:
    quantity=int(input("Enter the number of numbers: "))
    if quantity == 1:
        print(one_number())
    elif quantity == 2: 
        print(two_numbers())
    elif quantity>2:
        print(set_of_numbers())
    else:
        print('Please enter the correct value')

