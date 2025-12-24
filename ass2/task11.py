# binary to decimal
num = int(input("Enter a binary number "))
n = num
p=0
dec=0
while num>0:
	r = num%10
	dec = dec + r*2**p
	p=p+1
	num=num//10
print(n,"=",dec)
