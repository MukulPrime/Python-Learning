# program for Reverse Number as string 
def main():
    number = input("Enter a number: ")

    for digit in reversed(number):
        print(digit,end="")
    
main()