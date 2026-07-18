# Program for Multiplication Table up to 10
def main():
    table = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")

main()