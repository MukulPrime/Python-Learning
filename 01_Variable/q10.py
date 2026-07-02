# calculate BMI
def bmi_calculator():
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meter): "))
    
    bmi = weight / height**2

    print(f"Your BMI is : {bmi:.2f}")

bmi_calculator()