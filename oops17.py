"""
Write a python program to create a class Employee. In Employee class take two instance variables empid and empname. In Employee class create two methods setEmployee() and getEmployee(). setEmployee() method is used to initialize instance variables empid and empname whereas getEmployee() method is used to display values of empid and empname. By inheriting Employee class create a new class Payroll. In Payroll class create three instance variables bs, hra and da. In Payroll class create two methods setPayroll() and getPayroll(). setPayroll() method is used to initialize variables bs, hra and da whereas getPayroll() method is used to display values of bs, hra and da. Now by inheriting Payroll class create a new class Payslip. In Payslip class create a method named netSalary() which displays net salary with addition of basic salary, hra and da. Now test Payslip class. This is an example of multilevel inheritance.

In program (3) create a class Loan before the code of Payslip class. In Loan class create a method setLoan() which is used to initialize amt variable. Now inherit Loan class in Payslip class and in netSalary() method also print salary on hand as (bs+hra+da-amt). This is an example of hybrid inheritance.
"""
class Employee():
	def setEmployee(self,empid,empname):
		self.empid=empid
		self.empname=empname
	def getEmployee(self):
		print("Emp ID : ",self.empid)
		print("Emp Name : ",self.empname)
class Payroll(Employee):
	def setpayroll(self,bs,hra,da):
		self.bs=bs
		self.hra=hra
		self.da=da
	def getpayroll(self):
		print("Bs : ",self.bs)
		print("HRA : ",self.hra)
		print("DA : ",self.da)
class Loan():
	def setLoan(self,amt):
		self.amt = amt
		
class Payslip(Payroll,Loan):
	def netsalary(self):
		return self.bs+self.hra+self.da-self.amt

p=Payslip()
p.setEmployee(2,"Rohan")
p.getEmployee()
p.setpayroll(900,230,170)
p.getpayroll()
p.setLoan(490)
print("Net Salary : ",p.netsalary())




