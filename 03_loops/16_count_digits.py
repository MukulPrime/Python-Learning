# program for count digit 
def main():
    num = int(input("Enter the numbers: "))

    count = 0

    while num > 0:
        num = num // 10
        count += 1

    print(count)

main()