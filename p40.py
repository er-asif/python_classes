"""
sentence = input("Enter a line ")
find_what = input("Find what ?? ")
replace_with = input("Replace with ?? ")

new = sentence.replace(find_what,replace_with)
print(sentence)
print(new)



sent = "   The sun rises, in the east.   "
print(sent)
sent = sent.strip() # removes whitespaces from starting & ending
words = sent.split(" ") # returns a list, based on the separator

print(sent)
print(words)

print("Word count =",len(words))
print("Character count =",len(sent))

ch = 0
ws = 0
for c in sent:
	if c.isspace():
		ws+=1
	else:
		ch+=1
print(ch,ws)


characters = []
for c in sent:
	if not c.isspace():
		characters.append(c)
print(characters)


lst = ["Riya","John","Alice","Jonathan"]

s = ", ".join(lst)
print(s)


name = input("Enter name : ").lower().strip()
print("Palindrome" if name == name[::-1] else "Not Palindrome")
"""

n = int(input("Enter a number "))

print("Binary =",bin(n)[2:])
print("Octal =",oct(n)[2:])
print("Hexadecimal =",hex(n)[2:])


take full name as input & print short name
Mohammad Asif Ansari = M. A. Ansari
Mohammad Asif = M. Asif
Asif = Asif















