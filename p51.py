"""
with open("first.txt","a") as f:
	id = input("Enter ID :")
	name = input("Enter Name :")
	dep = input("Enter Department")
	age = int(input("Enter Age :"))
	f.write(f"\n\nID - {id}\nName - {name}\nDepartment - {dep}\nAge - {age}")
	print("Data Appended Sucessfully")
"""

f = open("first.txt","a")
id = input("Enter ID :")
name = input("Enter Name :")
dep = input("Enter Department")
age = int(input("Enter Age :"))
f.write(f"\n\nID - {id}\nName - {name}\nDepartment - {dep}\nAge - {age}")
print("Data Appended Sucessfully")
f.close()

