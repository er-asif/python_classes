# Destructor
# Destructor is a special type of method which is used to destroy the object and free the resources used by it.

class Myclass():
	def __init__(self,name):
		self.name = name
		print("Object is created and data is stored")
	def sayhello(self):
		print("Hi")
	def __del__(self):
		print(f"{self.name} object is destroyed")
	def __str__(self):
		return f"{self.name} ka Object"

obj = Myclass("Aman")
obj.sayhello()
print(obj)

