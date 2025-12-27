def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

# for n in infinite_numbers():
#     if n > 5:
#         break
#     print(n)

gen = infinite_numbers()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

