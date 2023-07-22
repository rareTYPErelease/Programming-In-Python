import math

# Define the Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    # Calculate and return the area of the circle
    def area(self):
        area = math.pi * self.radius * self.radius
        return area
    
    # Calculate and return the circumference (perimeter) of the circle
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

# Create a Circle object with a radius of 21
getArea = Circle(21)
# Calculate and print the area of the circle
print("Area of the circle with radius 21:", getArea.area())

# Create a Circle object with a radius of 21
getCircumference = Circle(21)
# Calculate and print the circumference (perimeter) of the circle
print("Circumference (Perimeter) of the circle with radius 21:", getCircumference.perimeter())
