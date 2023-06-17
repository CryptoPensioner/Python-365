# Task 12: Create a class called `Square` that represents a square object. 
# The `Square` class should inherit from a `Rectangle` class (from the previous lesson) 
# and add a method called `is_square()` that checks if the rectangle is actually a square by comparing its width and height. 
# Create a square object and test the `calculate_area()`, `calculate_perimeter()`, and `is_square()` methods.

# Task 11 Solution
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# Task 12 Solution
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False
        
rectangle1 = Rectangle(10, 20)
rectangle2 = Square(10)

print(rectangle1.calculate_area())
print(rectangle1.calculate_perimeter())
print(rectangle2.calculate_area())
print(rectangle2.calculate_perimeter())
print(rectangle2.is_square())
