'''
Function :-
	Function is a block of code which is used to perform a specific task. We can create a function and call it from any desired part of program.

	By using function we can achieve reusability of code.

# define
def fun():
	#function body
#calling
fun()

Types of functions:-

1. Predefined
  => print(), int(), input(), type(), etc.
2. User Defined
  => 


On the basis of parameter :-
1. Parameterized function
2. Non-parameterized function

On the basis of return type :-
1. Return type function
2. Non-return type function

'''

def greet():
	print("Good afternoon")

greet()

def greet(name):
	print("Good Afternoon",name)

greet("Suyash")
greet("Anish")


def greet():
	return "Good afternoon"

print(greet())


def greet(name):
	return "Good afternoon "+name

print(greet("Mohammad Asif Ansari"))
























