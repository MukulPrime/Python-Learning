# largest number among two
def largest_no():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    if number1 == number2:
        print("Both numbers are equal.") 
    elif number1 > number2:
        print(f"{number1} is the largest number.")
    else :
        print(f"{number2} is the largest number.")

largest_no()