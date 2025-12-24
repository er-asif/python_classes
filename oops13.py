# Abstraction :-
# Abstraction is a core principle of OOP which includes hiding unnecessory information and showing only necessory information.

# In python abstraction is achieved by using Abstract Base Class and abstract method.

from abc import ABC, abstractmethod
class Shape(ABC):
	@abstractmethod
	def area(self):
		pass
	@abstractmethod
	def peri(self):
		pass

class Circle(Shape):
	def __init__(self,r):
		self.r = r
	def area(self):
		return 3.14 * self.r**2
	def peri(self):
		return 2 * 3.14 * self.r

class Rectangle(Shape):
	def __init__(self,l,b):
		self.l = l
		self.b = b
	def area(self):
		return self.l * self.b
	def peri(self):
		return 2 * (self.l + self.b)


cir = Circle(3)
print("Area of Circle = ",cir.area())
print("Perimeter of Circle = ",cir.peri())

rect = Rectangle(3,4)
print("Area of Rectangle = ",rect.area())
print("Perimeter of Rectangle = ",rect.peri())



