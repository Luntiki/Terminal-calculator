from functions import *

def main():
    print('What do you want to spend? operations for a single number (ofs) or operations for two numbers (oft) or operations for multiple numbers(ofm)')
    main_action=input("Please write your action in a small format: ")
    if main_action == "ofs":
        return one_number()
    elif main_action == "oft":
        return two_numbers()
    elif main_action == "ofm":
        return set_of_numbers()
    else:
        print("Error. Please enter the correct value")
        return main()

while True:
    print(main())