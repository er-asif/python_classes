# reverse of a number
# 123 => 321
num = int(input("Enter a Number :"))
num2 = num
rev = 0
while num>0:
	r = num%10
	rev = rev*10 + r
	num=num//10
print("Reverse of",num2,"=",rev)