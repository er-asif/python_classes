"""
# Exception Handling in Python

Exception :- Abnormal termination of program is known as exception which terminate the execution in runtime.
These exceptions can be handled using try, except and finally block.
This is called exception handling.

"""
try:
	a = int(input("Enter first Number : "))
	b = int(input("Enter second Number "))
	div = a/b
	print(div)
except ValueError:
	print("Only intergers are allowed")
except ZeroDivisionError:
	print("Cannot divide by zero")
finally:
	print("Code executed successfully.")

Create an existing dictionary and take a word as input from user and find the meaning of that word in dictionary(handle KeyError).

dictionary = {}





















