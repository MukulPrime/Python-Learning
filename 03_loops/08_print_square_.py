# program for square of numbers
def main():
    number = int(input("Enter a number: "))
    for number in range(1, number+1) :
        print(f"the square of {number} is {number*number}")
main()