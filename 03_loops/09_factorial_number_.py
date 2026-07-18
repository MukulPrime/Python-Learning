# program for factorial of number
def main():
    number = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    
    print(f"{number}! = ", end="")

    for j in range(number,0,-1):
        print(j, end="")
        if j != 1:
            print("x", end="") 

    print(f" = {factorial}", end="")

main()