"""
# Polymorphism
# 'Poly'=> many + 'Morph'=> forms
# Forms mean functionalities or logics.
#The concept of defining multiple logics to perform some operation is known as a polymorphism.

Types of Polymorphism
1. Method Overloading

class Shape
{
	public int area(side)
	{
		return side*side
	}
	public int area(length,breadth)
	{
		return length*breadth
	}
}


2. Method Overriding

class Square
{
	public int area(side)
	{
		return side*side
	}
}	

class Rectangle extends Square
{
	public int area(length,breadth)
	{
		return length*breadth
	}
}

"""










# Method overloading  
# Python do not support Method overloading natively.
class Shape:
	"""
	def area(self,a=None,b=None):
		if a is not None and b is None:
			return a**2
		elif a is not None and b is not None:
			return a*b
	"""
	def area(self,*args):
		if len(args)==1:
			return args[0]**2
		elif len(args)==2:
			return args[0]*args[1]
sq = Shape()
print("Area of Square=",sq.area(5))
print("Area of Rectangle=",sq.area(5,6))














