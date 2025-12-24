# Strings in Python
# Set of characters
# Immutable
# Indexed

name = 'Aman Chaurasiya'
print(type(name))
name = "Virat Kohli"

#slicing
length = len(name)
print(name[:])
print(name)

#multiline string
 
poem = """Twinke twinkle, little star
How I wonder what you are"""
print(poem)


# Iteration 
player = "Virat Kohli"
for c in player:
	print(c)

rev = ""
for c in player:
	rev = c + rev
print(rev)

print(player[::-1])





















