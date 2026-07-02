# Calculate Total Marks and Average for 4 subject 
def calculate_marks():
    math = float(input("Enter your Mathematics marks: "))
    english = float(input("Enter your English marks: "))
    science = float(input("Enter your Science marks:  "))
    history = float(input("Enter your History marks: "))

    total_marks = math + english + science + history 
    average = total_marks / 4

    print(f"Total Marks is: {total_marks:.2f}")
    print(f"Average Marks is: {average:.2f}") 

calculate_marks()
