# Handling file not found exception

filename = input("Enter file name : ")
f = None
try:
	f = open(filename,"r")
	data = f.read()
	print(data)
except FileNotFoundError:
	print("this file doesn't exists.")
finally:
	if f is not None:
		f.close()
	