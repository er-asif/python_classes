dict1 = {'one':"First element"}
print(dict1['one'])
print(dict1.get('six'))

#adding element in dictionary
dict1["two"] = "Second element" 
dict1.update({3:'Three',4:'four'})

print(dict1)

# Traversing over a dictionary
for k in dict1:
	print(k,"=",dict1[k])
for k,v in dict1.items():
	print(k,v)


dict2 = {
     1:"One",
     2:"Two"
}
if 1 in dict2:
	print("Present")
else:
	print("Not present")




























