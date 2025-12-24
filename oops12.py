#
class Animal():
	def __init__(self,name,sound):
		self.name = name
		self.sound = sound
class Dog(Animal):
	def __init__(self,name,sound,breed):
		super().__init__(name,sound)
		self.breed=breed
	def make_sound(self):
		print(f"{self.name} says {self.sound} and is a {self.breed}")

d = Dog("Tommy","Bark..","German Sherfered")
d.make_sound()