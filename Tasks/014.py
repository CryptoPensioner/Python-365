# Task 14: Create a class called Animal with a method make_sound() that prints a generic sound. 
# Create two derived classes, Cat and Dog, that inherit from Animal. 
# Override the make_sound() method in each derived class to print the specific sound of a cat and a dog, respectively. 
# Create objects of both derived classes and call the make_sound() method on each object.

class Animal():
    def make_sound(self):
        print("Grrr")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

cat = Cat()
dog = Dog()

cat.make_sound()
dog.make_sound()
