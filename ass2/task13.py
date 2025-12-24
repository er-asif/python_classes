ll = int(input("Enter lower limit of range "))
ul = int(input("Enter upper limit of range "))

for n in range(ll,ul+1):
	c=0
	i=1
	while i<=n:
		if n%i==0:
			c=c+1
		i=i+1
	if c==2:
		print(n)
