# Example of Method Overriding

class Vehicle:
    def start(self):
        print("Starting Vehicle.")

class Car(Vehicle):
    def start(self):
        print("Starting car with key.")

obj = Car()

obj.start()

# Example of Method Overloading

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a+b+c
    
obj = Calculator()

print(obj.add())
print(obj.add(10))
print(obj.add(10,20))
print(obj.add(10, 20, 25))

#Default Constructor

class Demo:
    def __init__(self):
        print("Default constructor called")

d = Demo()

#Parameterized Constructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Rohit", 18)
print(s.name)
print(s.age)

# Constructor with default Arguments

class Example:
    def __init__(self, a=None, b=None):
        print(a, b)

e1 = Example(10)
e2 = Example(10, 20)
