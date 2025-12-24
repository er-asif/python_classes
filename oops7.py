# Multiple Inheritance 
# When a class inherit more than one classes at the same time then, this is known as Multiple Inheritance.

class A():
	def m1(self):
		print("M1 from class A")
class B():
	def m2(self):
		print("M2 from class B")
class C(A,B):
	def m3(self):
		print("M3 from class C")
obj = C()
obj.m1()
obj.m2()
obj.m3()