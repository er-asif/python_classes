"""
take full name as input & print short name
Mohammad Asif Ansari = M. A. Ansari
Mohammad Asif = M. Asif
Asif = Asif
"""
fullname = input("Enter Full Name ").title()
words = fullname.split(" ") 
shortname = ""
for n in words[0:len(words)-1]: 
	shortname = shortname + n[0] + ". "  

shortname = shortname + words[-1]
print(shortname)
















