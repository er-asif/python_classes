s1 = input("Enter 1st string ").lower().strip()
s2 = input("Enter 2nd string ").lower().strip()
if sorted(s1) == sorted(s2):
	print(sorted(s1))
	print(sorted(s2))
	print("Anagram")
else:
	print(sorted(s1))
	print(sorted(s2))
	print("Not Anagram")




