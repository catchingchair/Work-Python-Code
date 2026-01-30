
# practicing objects and classes

class Dog: # a class is like a "blueprint" for creating objects
    def __init__(self, name = "Unknown Dog", age = None): 
        # the __init__ method is used to assign values to object properties or to perform operations that are necessary when the object is being created. 
        # we can assign default values in the parameters.
        self.name = name
        self.age = age
    def bark(self):
        print("woof!")

dog1 = Dog("spot", 100)
print(f"{dog1.name} is {dog1.age} years old.")

dog2 = Dog()
print(f"{dog2.name} is {dog2.age} years old.")

# Q: what if we did not have the __init__ method?
# A: we would have to set properties manually for each object. 

class Plane:
    pass # we can use pass as a "null operation" or a "placeholder" to define an empty class. 
         # this allows us to not have to define any attributes or methods. 

plane1 = Plane()
plane1.wingspan = 100
plane1.weight = 5000

print(f"{plane1.wingspan} and {plane1.weight}")

# we DELETE objects using the "del" keyword
# in most cases we won't delete objects because of Python's automatic memory management (garbage collection).
del plane1

# Practice Part 2: Student info
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
    def display_info(self):
        print(f"Student Name: {self.name}\nStudent ID: {self.student_id}")

student1 = Student("Trent",634086)
student1.display_info()


#Practice Part 3 Rectangle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return (self.width*2) + (self.height*2)
    
    def display_calculations(self):
        print(f"The area is {self.area()}. The perimiter is {self.perimeter()}")

rectangle1 = Rectangle(10,10)
rectangle1.display_calculations()

# Level 2: Methods & State

# 4. Bank Account
# 
# Create a class BankAccount with:
# Attributes: owner, balance
# Methods:
# deposit(amount)
# withdraw(amount) (don’t allow balance to go negative)

# 5. Counter
#
# Create a class Counter that:
# Starts at 0
# Has methods:
# increment()
# decrement()
# reset()

# 6. Book Tracker
# 
# Create a class Book with:
# Attributes: title, author, is_checked_out
# Methods:
# check_out()
# return_book()