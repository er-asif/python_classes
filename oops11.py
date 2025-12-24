# Method Overrding
class Square():
	# 1000 more methods
	def area(self,s):
		return s**2
class Rectangle(Square):
	# 1000 methods
	def area(self,l,b):
		return l*b

sq = Square()
print("Area of Square =",sq.area(5))

rect = Rectangle()
print("Rectangle of Square =",rect.area(4,5))