# Program to check pass or fail 
def pass_fail():
    marks = float(input("Enter your marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks.")
    elif marks >= 40 :
        print("Pass")
    else:
        print("Fail") 
         
pass_fail()