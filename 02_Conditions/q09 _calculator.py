# A real calculator program 
def calculator():
    number1 = int(input("Enter the first number: "))
    operator = input("select operator(+,*,/,-): ")
    number2 = int(input("Enter the second number: "))

    if operator == "/" and number2 == 0:
        print("Cannot divide by zero.")
    elif operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    elif operator == "/":
        print(number1 / number2)
    else:
        print("Invalid operator.")

calculator()

