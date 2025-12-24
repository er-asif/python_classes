# Encapsulation ?
# In Python, encapsulation is a way to restrict access to certain components of 
# an object to prevent the accidental modification of data.
# or
# Wrapping of data into a single unit is called encapsulation.

class Car():
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color

    def display(self):
        print(f"""Car Name = {self.name}
Model = {self.model}
Color = {self.color}
""")
        
scorpio = Car("Mahindra Scorpio","N - 2025", "Z-black")
scorpio.display()

bmw = Car("BMW", "M4","Black")
bmw.display()
