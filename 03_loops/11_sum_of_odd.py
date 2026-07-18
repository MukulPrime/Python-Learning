# program to add odd numbers
def main():
    number = int(input("Enter a number: "))
    total = 0
    for i in range(1,number+1,2):
         total += i
    print(f"Sum of odd numbers up to {number} is ",end="")

    for j in range(1,number+1,2):
         print(j, end="")
         if number >= j+2:
              print("+",end="")
           

    print(" =" ,total)
        
main()