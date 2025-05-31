from functions import one_number, two_numbers

while True:
    quantity=int(input("Enter the number of numbers: "))
    if quantity == int(1):
        print(one_number())
    elif quantity == 2: 
        print(two_numbers())
    else:
        print('Please enter the correct value')