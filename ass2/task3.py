import cmath
a = int(input("Enter coefficient of x^2 "))
b = int(input("Enter coefficient of x "))
c = int(input("Enter constant "))
#d = b**2 - 4*a*c
#if d<0:
	#print("Roots are imaginary")
#else:
root1 = (-b+cmath.sqrt(b*b-4*a*c))/(2*a)
root2 = (-b-cmath.sqrt(b*b-4*a*c))/(2*a)
print("Root1 =",root1)
print("Root2 =",root2)