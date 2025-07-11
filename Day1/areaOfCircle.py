import math
def getArea(radius:int):
    return math.pi*radius**2

radius = int(input("Enter the radius of the circle "))
print(f"The area of the circle is {getArea(radius)}")