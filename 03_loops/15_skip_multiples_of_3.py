# Program to skip multiple of 3 
def main():
    num = int(input("Enter a number: "))

    for x in range(1,num+1):
        if num % 3 == 0:
            continue
        print(num)

main()