# check whether a number is positive or negative or zero 
def positive_negative():
    number = int(input("Enter the number: "))

    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else :
        print("Number is zero")

positive_negative()