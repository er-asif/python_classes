import os
import random
import math
import datetime

print(os.getcwd())

lst = os.listdir()
tup = tuple(lst)
# # for file in lst:
# #     print(file)

# # os.rename("old_file_name","new_file_name")
# os.rename('p611.py','p61.py')


# os.remove('p61.py')

otp = random.randint(1000,9999)
print("OTP Genarated : ",otp)

print("HCF =",math.gcd(2,10))
print("LCM =",math.lcm(2,10))

print(math.hypot(3,4))

otp = ""
for i in range(4):
    otp += str(random.randint(0,9))
print("OTP =",otp)

pahle = datetime.datetime.now()
for file in lst:
    print(file)
print(pahle)
print(datetime.datetime.now()-pahle)