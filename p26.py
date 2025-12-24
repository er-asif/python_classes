"""
#import random
#import random as rn
from random import randint

#print(randint(1,10))
#print(randint(1000,9999))

num = randint(1,10)

while True:
	guess = int(input("Guess the number b/w 1-10: "))
	if num==guess:
		print("You won")
		break
	else:
		print("Better luck!! next time!!")



from random import shuffle,choice

names = ['Atul','Akram','Aman','Ajay','Rimjhim','Suyash']
print(choice(names))

"""

name = input("Enter Name ")
s = f"Hi everyone, My name is {name}"
print(s)















