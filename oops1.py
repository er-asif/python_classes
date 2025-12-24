"""
OOPS :-
	Object Oriented Progamming System is a mechanism for software development. By using OOPS we can make more secure, reliable softwares applications. It enhances the security and reusability.

There are classes and objects.

Pillers of OOPs:
	1. Encapsulation
	2. Inheritance
	3. Polymorphism
	4. Abstraction


Class :- Class is a collection of data member and member functions.
	It is blueprint of objects.

Object :- Object is an instance of a class. It has methods and properties which were defined in the class.
Memory is allocated to objects as it is created.


Static/class Variables

The variables which are declared within the class, outside of all the methods are known as static variables 
(or) class variables.
The data which is common for every object is recommended to represent by using static variables.
For all the static variables of a class, memory will allocated only once.
Static variable of one class can access within the same class (or) outside of the class by using class name.

Non-static/object/instance Variables

The variables which are declared with self (or) reference variable are known as non-static variables (or) 
instance variable.
Non static variables we can define within the constructors (or) within the method.
The data which is separate for every object is recommended to represent by using non-static variable.
For all the non-static variables of a class, memory will be allocated whenever we create object.
With respect to every object creation statement separate copy of memory will be allocated for non-static 
variable.
Non static variable of one class, we can access within the same class by using ‘self’.
Non static variables of one class we can access outside the class by using reference variable name.


"""

# Defining a class
# First character uppercase

class Trainees():
	company = "Softpro India"

	def training(self):	
		print("Training.......started.....")

atul = Trainees()
print(atul.company)
atul.training()

saif = Trainees()
print(saif.company)
saif.training()

print(id(atul))
print(id(saif))

































