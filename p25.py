string = input("Enter a string ")
# string the sun rises in the east
v = ['a','e','i','o','u']
vowels = {}
for c in string:
	if c in v:
		if c in vowels:
			vowels[c] = vowels[c]+1
		else:
			vowels[c] = 1
for k,v in vowels.items():
	print(k,"=",v)