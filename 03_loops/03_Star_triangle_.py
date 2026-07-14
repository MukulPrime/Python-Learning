# program for star traingle using loops
def main():
    rows = int(input("Enter rows: "))
    for i in range(rows):
        for j in range(i + 1):
            print("*", end="")
        print()

main()
    