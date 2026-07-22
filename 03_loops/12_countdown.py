# Program for Reverse countdown
def main() -> None:
    number = int(input("Enter a number: "))

    for i in reversed(range(0, number+1)):
        print(i)

    print("Blast off!")

main()