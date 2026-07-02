# Calculating simple interest
def simple_interest():
    P = float(input("Enter the Principal amount: "))
    R = float(input("Enter the total of rate of Interest: "))
    T = float(input("Enter the total time period(in years): "))

    interest = P*R*T/100

    print(f"SIMPLE INTEREST IS: {interest:.2f} ")

simple_interest()