# Convert second into minutes 
def time_converter():
    seconds = float(input("Enter the second to convert: "))
    minutes = seconds / 60

    print(f"{seconds} seconds = {minutes:.2f} minutes")

time_converter()

    