file = open("first.txt", "w")

file.write("""ID - SPI-2140
Name - Mohammad Asif
Department - IT
Age - 28
""")
file.close()
print("Operation Performed")


file = open("first.txt", "r+")
data = file.read()
print(data)
file.write("Hello")
file.close()