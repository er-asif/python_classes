class Employee():
	company = "Softpro India"
	def __init__(self,id,name,salary):
		self.empid = id
		self.empname = name
		self.salary = salary
	def showinfo(self):
		print("Company Name -",self.company)
		print("ID -",self.empid)
		print("Name -",self.empname)
		print("Salary -",self.salary)

brijesh = Employee("SPI-2120","Brijesh Mishra", "7crore")
brijesh.showinfo()

asif = Employee("SPI-2140", "Mohammad Asif", "25crore")
asif.showinfo()

