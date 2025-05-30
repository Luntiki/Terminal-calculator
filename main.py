from functions import one_number, two_numbers

quantity=abs(int(input("Enter the number of numbers: ")))

if quantity == 1:
    print(one_number())
elif quantity == 2:
    print(two_numbers())
else:
    print()
