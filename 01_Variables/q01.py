#ask user for it's name and age 
def user_info():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    print(f"Hello, {name} you are {age} years old.")
    print("GOOD BOY!")

user_info()