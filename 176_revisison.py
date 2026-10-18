# Problem Statement:
# Write a Python program that takes a string from the user
# and counts the frequency of each character in the string.
#
# Ignore spaces and treat uppercase and lowercase letters as the same.
#
# Example:
# Input: Hello World
# Output:
# h: 1
# e: 1
# l: 3
# o: 2
# w: 1
# r: 1
# d: 1
#
# Hint:
# Use a dictionary to store the character frequencies.
#
# Your Task:
# Take a string as input and print the frequency of each character.


text = input("Enter a string: ").lower()

frequency = {}

for char in text:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

for char, count in frequency.items():
    print(char, ":", count)