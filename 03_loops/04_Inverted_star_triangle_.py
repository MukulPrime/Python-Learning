# program for inverted star triangle
def main():
    rows = int(input("Enter number of rows: "))
    for i in range(rows):
        for j in range(rows - i):
            print("*" , end = " ")
        print()

main()
