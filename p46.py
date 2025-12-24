"""
Create an existing dictionary and take a word as input from user and find the meaning of that word in dictionary(handle KeyError).
"""
from words_meanings import dictionary

word = input("Enter a word to search : ")
try:
	print("Meaning =", dictionary[word])
except KeyError:
	print("Word not found in dictionary !!")


