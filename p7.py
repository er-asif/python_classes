unit = int(input("Enter units :"))
if unit<=150:
	bill = unit*2.4
elif unit>150 and unit<=300:
	bill = 150*2.4 + (unit-150)*3.00
else:
	bill = 150*2.4 + 150*3.00 + (unit-300)*3.2
print("Total Bill =",bill)