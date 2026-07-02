# Calculate Total Marks and Average for 4 subject 
def calculate_marks():
    subject1 = float(input("Enter your subject1 marks: "))
    subject2 = float(input("Enter your subject2 marks: "))
    subject3 = float(input("Enter your subject3 marks: "))
    subject4 = float(input("Enter your subject4 marks: "))

    total_marks = subject1 + subject2 + subject3 + subject4 
    average = total_marks / 4

    print(f"Total Marks is: {total_marks:.2f}")
    print(f"Average Marks is: {average:.2f}") 

calculate_marks()
