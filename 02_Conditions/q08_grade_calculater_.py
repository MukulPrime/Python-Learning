# Grade calculater program
def grade_calculator():
    marks = int(input("Enter your marks (0-100): "))

    if marks > 100 or marks < 0 :
        print ("Invalid Marks. ")
    elif marks >= 90 :
        print("You got grade A+ .")
    elif marks >= 80 :
        print("You got grade A. ")
    elif marks >= 70 :
        print("You got grade B. ")
    elif marks >= 60 :
        print("You got grade C. ")
    elif marks >= 50 :
        print("You got grade D. ")
    elif marks >= 40 :
        print("You got grade E. ")
    else:
        print("Result : FAIL. ")

grade_calculator()    