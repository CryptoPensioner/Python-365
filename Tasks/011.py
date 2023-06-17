# Task 11: Create a class called `Rectangle` that represents a rectangle object. 
# The class should have attributes `width` and `height`, and methods `calculate_area()` 
# and `calculate_perimeter()` to compute the area and perimeter of the rectangle, respectively. 
# Create two rectangle objects and test the methods.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rectangle1 = Rectangle(5, 10)
rectangle2 = Rectangle(10, 20)

print(rectangle1.calculate_area())
print(rectangle1.calculate_perimeter())
print(rectangle2.calculate_area())
print(rectangle2.calculate_perimeter())
