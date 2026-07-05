    # BMI calculator category wise
def bmi_calculator():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        print(f"Your BMI is {bmi:.2f} ",end = "\nYou are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi:.2f} ",end ="\nYou are healthy.")
    elif bmi < 30:
        print(f"Your BMI is {bmi:.2f} ",end ="\nYou are overweight.")
    else:
        print(f"Your BMI is {bmi:.2f}",end ="\nYou have obesity.")

bmi_calculator()