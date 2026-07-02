# Converting the temperature from celsius to fahrenheit 
def temp_converter():
    celsius = float(input("Enter the value of celsius: "))
    fahrenheit = (celsius * 9/5)+32

    print(f"The value of Fahrenheit is: {fahrenheit:.2f}  ")

temp_converter()    