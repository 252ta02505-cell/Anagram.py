# Anagram.py

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

# Check whether the strings are anagrams
if sorted(str1) == sorted(str2):
    print("The given strings are Anagrams.")
else:
    print("The given strings are not Anagrams.")
