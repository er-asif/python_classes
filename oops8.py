# Hierarachial Inheritance

class A:
	def m1(self):
		print("M1 from class A")
class B(A):
	def m2(self):
		print("M2 from class B")
class C(A):
	def m3(self):
		print("M3 from class C")
class D(B):
	def m4(self):
		print("M4 from class D")
class E(B):
	def m5(self):
		print("M5 from class E")
class F(C):
	def m6(self):
		print("M6 from class F")
class G(C):
	def m7(self):
		print("m7 from class G")

objE = E()
objE.m1()
objE.m2()
objE.m5()
#objE.m4() This will through AttributeError

objG = G()
objG.m1()
objG.m3()
objG.m7()


