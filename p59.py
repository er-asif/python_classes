import json 
data = {
    "empid" : "SPI-2140",
    "empname" : "Mohammad Asif",
    "designation" : "Software Engineer",
    "department" : "IT",
    "age" : 28
}

file = open("emp.json","w+")
json.dump(data,file,indent=4)
print("data is added")

file.seek(0)
data = json.load(file)
print(data)

file.close()