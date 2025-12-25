# Class, object & Constructor, Destructor

class Employee:
	company = "Softpro India"
	def __init__(self,id,name,age):
		print("Object created")
		self.empid = id
		self.empname = name
		self.age = age

	def display(self):
		print("Company : ",self.company)
		print("Id : ",self.empid)
		print("Name : ",self.empname)
		print("Age : ",self.age)

	def __del__(self):
		print("Object destroyed")
	
e=Employee(1001,"Sohan Tiwari",24)
e.display()


