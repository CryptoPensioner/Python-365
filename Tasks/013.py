# Task 13: Refactor the Rectangle class (from a previous lesson) to encapsulate the width and height attributes by marking them as private. 
# Create getter and setter methods (get_width(), get_height(), set_width(), set_height()) to access and modify the attributes. 
# Test the getter and setter methods by creating a Rectangle object, setting its width and height, and retrieving their values.

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def calculate_area(self):
        return self.__width * self.__height
    
    def calculate_perimeter(self):
        return 2 * (self.__width + self.__height)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def is_square(self):
        if self.get_width() == self.get_height():
            return True
        else:
            return False
        
rectangle1 = Rectangle(10, 20)
rectangle2 = Square(10)

print(f"Rectangle 1 Area: {rectangle1.calculate_area()}")
print(f"Rectangle 1 Perimeter: {rectangle1.calculate_perimeter()}")
print(f"Rectangle 2 Area: {rectangle2.calculate_area()}")
print(f"Rectangle 2 Perimeter: {rectangle2.calculate_perimeter()}")
print(f"Is Rectangle 2 a Square: {rectangle2.is_square()}")

rectangle3 = Rectangle(10, 20)
rectangle3.set_width(33)
rectangle3.set_height(33)
print(f"Rectangle 3 Area: {rectangle3.calculate_area()}")
print(f"Rectangle 3 Perimeter: {rectangle3.calculate_perimeter()}")
rectangle3 = Square(10)
print(f"Is Rectangle 3 a Square: {rectangle3.is_square()}")
print(f"Rectangle 3 Area: {rectangle3.calculate_area()}")
print(f"Rectangle 3 Perimeter: {rectangle3.calculate_perimeter()}")
