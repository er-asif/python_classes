"""
# expression
num = 5
is_even_or_odd = lambda x : "Even" if x%2==0 else "Odd"
print(is_even_or_odd(num))


# [expression for item in iterable if condition]

lst = [1,2,3,4]
evens = [n**2 for n in lst]
print(lst)
print(sq)
"""


# Filter()
# used to select subset from a collection based on a function returns True
numbers = [1,2,3,4,5,6,7,8,9,10]

def is_even(n):
	return n%2==0
def is_odd(n):
	return n%2==1

even_numbers = list(filter(is_even,numbers))
odd_numbers = list(filter(is_odd,numbers))

print(even_numbers)
print(odd_numbers)


# map()
# used to perform operation on each elements of collection and return new collection

numbers = [1,2,3,4,5,6,7,8,9,10]
def sq(n):
	return n**2

squared = list(map(sq,numbers))
print(squared)



"""
List comprehension
Lambda function
map()
filter()
""""



















