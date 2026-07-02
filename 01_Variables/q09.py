# calculate salary with bonus percentage
def total_income():
    income = float(input("Enter your income: "))
    bonus  = float(input("Bonus percentage: "))

    salary = income + (bonus*income)/100

    print(f"Total income :{salary:.2f}")

total_income()

