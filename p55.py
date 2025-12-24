""" Constructor
# -----------------
# Constructor is a special type of method, which is called by itself as we create an object of any class.
# In python constructor is "__init__()".
# It helps in object memory allocation.

Types of Constructor:
	1. Default
	2. Parameterized

"""


class Human():
	def __init__(self,name):
		print(name,"Object created successfully")
	scientific_name = "Homo sapiens"
	def think(self):
		print("Thinkinggg.....")
	def talk(self):
		print("Talking........")

suyash = Human()















