#Variable length arguments

def sum(*args):
	s = 0
	for n in args:
		s=s+n
	return s

print(sum(2,10))

def result(**kwargs):
	for subject in kwargs.items():
		print(subject)

result(maths=23,dbms=25,java=12,python=45)

