"""
# Inheritance
# Inheriting the properties of one class in another class is known as Inheritance. 
# Base class (parent / super class ) 
# Derived class (Child / Sub class) 

# class Parent():
	# 1000 methods
# class Child(Parent):
	# 1000 methods
	# 500 methods
"""

class Parent():
	def sayhello(self):
		print("Hello, Everyone")
class Child(Parent):
	def saygoodbye(self):
		print("Good Bye")

c = Child()
c.sayhello()
c.saygoodbye()


"""
Types of Inheritance
	1. Single Level Inheritance
	2. Multi Level Inheritance
	3. Multiple Inheritance
	4. Hierarchial Inheritance
	5. Hybrid Inheritance

"""
















