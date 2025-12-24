import csv

f = open("data.csv", "r")
data = csv.reader(f)
for r in data:
	print(r)
f.close()