# program to add even numbers
def main():
    number = int(input("Enter a number: "))
    x = 0
    for i in range(2,number+1,2):
         x += i
    print(f"Sum of even numbers up to {number} is ",end="")

    for j in range(2,number+1,2):
         print(j, end="")
         if number!=j:
              print("+",end="")
           

    print(" =" ,x)
        
main()