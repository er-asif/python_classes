"""
groupA = {1,2,3}
print(groupA)
print(type(groupA))

groupA.add(15)
groupA.add(10)
groupA.remove(3)
print(groupA)


lst = [1,2,3,3,4,5,6,9,9]
print(lst)
set1 = set(lst)
print(set1)

"""

#Union

set1 = {1,2,3,4,9}
set2 = {1,2,10,12}

print(set1)
print(set2)
print(set1.union(set2))

#intersection
print(set1.intersection(set2))


set1 = {1,2,3,4}
set2 = {1,2}

print(set2.issubset(set1))
print(set1.issuperset(set2))











































