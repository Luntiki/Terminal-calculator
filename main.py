from functions import one_number, two_numbers

while True:
    try:
        quantity=abs(int(input("Enter the number of numbers: ")))
    except:
        print('Error. Please enter an intenger')
        if quantity == 1:
            print(one_number())
        elif quantity == 2: 
            print(two_numbers())