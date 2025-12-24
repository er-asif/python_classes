import json

file = open('n.json','r')

data = json.load(file)
# print(data['users'][0])
user1 = data['users'][0]

for k,v in user1.items():
    print(f"{k} = {v}")
    if k=="address":
        for k1,v1 in user1['address'].items():
            print(f"{k1} = {v1}")

file.close()