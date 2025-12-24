"""
Write a python program to create a class named Shape. In Shape class create a method named setValue(), this method initialize side of shape. By inheriting Shape class create a new class Square. In Square class create a method area(), this method return area of square. Now by inheriting Shape class create a new class Cube. In Cube class create a method volume(), this method return volume of cube. Now Test Square and Cube classes.
"""

class Shape:
	def setValue(self, a):
		self.a=a
class Square(Shape):
	def area(self):
		return self.a*self.a
class Cube(Shape):
	def volume(self):
		return self.a**3
s=Square()
s.setValue(5)
print("Area of Square:",s.area())

c=Cube()
c.setValue(4)
print("Volume of Cube",c.volume())


	
		