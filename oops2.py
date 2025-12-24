# Variables in class
class Employees():
	company = "Softpro Group of Companies"
	def setvalue(self,id,name,age):
		self.empid = id
		self.empname = name
		self.empage = age
	def display(self):
		print("Company :",self.company)
		print("ID :",self.empid)
		print("Name :",self.empname)
		print("Age :",self.empage)

manish = Employees()
manish.setvalue("SPI-2145","Manish Yadav",23)
manish.display()

asif = Employees()
asif.setvalue("SPI-2140","Mohd. Asif",22)
asif.display()



"""
employees = {
       {
	   'empid': "SPI-2145",
	   'empname': "Manish Yadav",
	   'empage' : 23
       },
       {
	   'empid': "SPI-2140",
	   'empname': "Mohd. Asif",
	   'empage' : 28
       }
}

"""


















