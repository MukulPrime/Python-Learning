# reverse countdown
def main():
    number = int(input("Enter a number: "))

    for i in reversed(range(1, number+1)):
        print(i)

    print("Blast off!")

main()