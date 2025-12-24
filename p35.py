"""
#traversal
# marks = [12,33,44]

dict1 = {
	'1001' : 33,
	'1002' : 34,
}

for k,v in dict1.items():
	print(k,v)

#adding 
dict1['1003'] = 22
dict1.update({'1004':26,'1005':39})
print(dict1)

#get an element 
#print(dict1['1009'])
print(dict1.get('1009'))



d = {}

for i in range(5):
	key = input("Enter key ")
	val = input("Enter value ")
	#d.update({key:val})
	d[key] = val
print(d)

"""

stu = {
	'ariz': "Mohd. Ariz",
	'anurag': "Anurag he poora h",
	'akram' : "Akram Jamal"
}

print(stu)
del stu['ariz']
print(stu)
stu.clear()
print(stu)



















