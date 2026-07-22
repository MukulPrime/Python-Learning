# Program to check wheather a number is palindrome or not
def main():
    num = int(input("Enter the number: "))
    
    palindrome = 0

    while num > 0:
        digit = num % 10
        palindrome = palindrome * 10 + digit
        num = num // 10 

    if palindrome == num:
        print("This number is palindrome")
    else:
        print("This number is not palindrome")
        
main()
