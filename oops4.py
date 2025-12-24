"""
Write a python program to create a class with name ‘Rectangle’. In ‘Rectangle’ class take two instance variables length and breadth. Now create a parameterized constructor to initialize variables and create a method area() which return area of rectangle. Test the class ‘Rectangle’.
"""

class Rectangle():
	def __init__(self,l,b):
		self.length = l
		self.breadth = b
	def area(self):
		return self.length*self.breadth

l = int(input("Enter length "))
b = int(input("Enter breadth "))
rect = Rectangle(l,b)
print("Area =",rect.area())



