#binary to decimal

binary = int(input("Enter a binary number : "))
p = 0
dec = 0
"""
while binary>0:
	d = binary%10
	dec = dec + d*2**p
	p+=1
	binary//=10
"""
for d in str(binary)[::-1]:
	print(d)
	dec = dec + int(d)*2**p
	p+=1
print(dec)