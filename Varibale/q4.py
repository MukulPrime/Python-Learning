#Calculate the area of circle
import math

def area_of_circle():
    Radius=float(input("Enter the radius of circle :"))
    area = math.pi * Radius**2

    print(f"Area of circle is :{area:.2f}") 

area_of_circle()    