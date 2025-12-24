num = int(input("Enter a Number "))
n=num
digit=0
while n>0:
	digit=digit+1
	n=n//10
n=num
arm=0
while n>0:
	r = n%10
	arm = arm + r**digit
	n=n//10
if arm == num:
	print("Number is Armstrong")
else:
	print("Number is NOT Armstrong")






