"""
create 2 functions ftoc(para, return) and ctof(para, return)
ftoc => Fahrenheit to Celsius  °F = (°C × 9/5) + 32
ctof => Celsius to Fahrenheit  °C = (°F - 32) × 5/9
"""

def ftoc(f):
	cel = (f - 32) * 5/9
	return cel

def ctof(c):
	fah = (c * 9/5) + 32
	return fah

print("Enter 1 for Celsius to Fahrenheit\nEnter 2 for Fahrenheit to celsius")
ch = input()

if ch=="1":
	c = eval(input("Enter temp in celsius "))
	print("Fahenheit = ",ctof(c))
elif ch=="2":
	f = eval(input("Enter temp in fahrenheit "))
	print("Celsius = ",ftoc(f))
else:
	print("Invalid choice.")

