# Multi-level Inheritance
# When there is more than one level in the inheritance then, this type pf inheritance is Multi-level Inheritance.

class A():
	def m1(self):
		print("M1 from class A")
class B(A):
	def m2(self):
		print("M2 from class B")
class C(B):
	def m3(self):
		print("M3 from class C")
obj = C()
obj.m1()
obj.m2()
obj.m3()
