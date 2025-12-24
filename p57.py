# import csv

# data = [
#     ['Name','Course','Year'],
#     ['Mohd. Asif','CSE','Final'],
#     ['Atul Sharma','IT','Final'],
#     ['Sruti Srivastava','CSE','3rd'],
#     ['Umar Ziddum ziddah','BCA','final'],
#     ['Farooq','MCS','1st']
# ]
# file = open("new_data.csv", "w+" ,newline='')
# w = csv.writer(file)
# w.writerows(data)

# file.seek(0)
# # loaded_data = csv.reader(file)
# loaded_data = csv.DictReader(file)
# for row in loaded_data:
#     print(row)

# file.close()


import pandas as pd
data = pd.read_csv('new_data.csv')
print(data)


# Pypi

# pip install library_name
# pip uninstall library_name