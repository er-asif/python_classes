import sys
nums_list = [x for x in range(1)]
nums_gen = (x for x in range(1))

print(sys.getsizeof(nums_list))  # Memory used by list
print(sys.getsizeof(nums_gen))   # Memory used by generator

