# swap of two numbers using a temporary varibale 
def swap_numbers(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    temp=a
    a=b
    b=temp
    print(f"After swapping: a = {a}, b = {b}")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
swap_numbers(a, b) 
