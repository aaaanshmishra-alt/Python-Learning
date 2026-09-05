# ============================================================
#                         PYTHON STRINGS
# ============================================================


# ------------------------------------------------------------
# 1. WHAT IS A STRING?
# ------------------------------------------------------------
# A String is a sequence of characters.
# Strings are written inside single or double quotes.

name = "Ansh"
city = 'Bangalore'

print(name)
print(city)


# Triple quotes can be used for multi-line strings.

message = """Hello
I am learning Python
I am studying Strings."""

print(message)


# ------------------------------------------------------------
# 2. STRING INDEXING
# ------------------------------------------------------------
# Strings are ordered and indexed.
# Indexing starts from 0.

name = "Ansh"

# A   n   s   h
# 0   1   2   3

print(name[0])    # A
print(name[1])    # n
print(name[2])    # s
print(name[3])    # h


# ------------------------------------------------------------
# 3. NEGATIVE INDEXING
# ------------------------------------------------------------
# Negative indexing starts from the right.
# The last character has index -1.

name = "Ansh"

# A   n   s   h
# -4 -3  -2  -1

print(name[-1])   # h
print(name[-2])   # s


# Remember:
#
# Positive index → starts from LEFT → 0
# Negative index → starts from RIGHT → -1


# ------------------------------------------------------------
# 4. STRING SLICING
# ------------------------------------------------------------
# Syntax:
#
# string[start:end]
#
# start → included
# end   → excluded

name = "Ansh"

print(name[0:2])
# An

print(name[1:4])
# nsh


# Start can be omitted:

print(name[:2])
# An


# End can be omitted:

print(name[2:])
# sh


# Both can be omitted:

print(name[:])
# Ansh


# ------------------------------------------------------------
# 5. STRINGS ARE IMMUTABLE
# ------------------------------------------------------------
# Strings cannot be changed character-by-character.

name = "Ansh"

# name[0] = "B"
# ❌ Error


# We can create a NEW string instead:

name = "Bnsh"

print(name)


# IMPORTANT:
# Strings are immutable.


# ------------------------------------------------------------
# 6. len()
# ------------------------------------------------------------
# len() returns the number of characters.

name = "Ansh"

print(len(name))
# 4


# Spaces also count as characters.

message = "Hello World"

print(len(message))


# ------------------------------------------------------------
# 7. LOOPING THROUGH A STRING
# ------------------------------------------------------------
# We can use a for loop to visit every character.

name = "Ansh"

for character in name:
    print(character)


# Output:
# A
# n
# s
# h


# ------------------------------------------------------------
# 8. STRING CONCATENATION
# ------------------------------------------------------------
# Strings can be joined using +.

first = "Ansh"
last = "Mishra"

name = first + " " + last

print(name)
# Ansh Mishra


# ------------------------------------------------------------
# 9. STRING + NUMBER
# ------------------------------------------------------------
# A String and a number cannot be directly combined using +.

age = 20

# print("Age: " + age)
# ❌ Error


# Convert the number to String:

print("Age: " + str(age))
# Age: 20


# ------------------------------------------------------------
# 10. STRING REPETITION
# ------------------------------------------------------------
# A String can be multiplied by an integer.

word = "Hi"

print(word * 3)
# HiHiHi


# ------------------------------------------------------------
# 11. MEMBERSHIP — in / not in
# ------------------------------------------------------------
# 'in' checks whether a character or substring exists.

word = "Python"

print("P" in word)
# True

print("th" in word)
# True

print("xyz" in word)
# False


# 'not in' checks that something does NOT exist.

print("xyz" not in word)
# True


# ------------------------------------------------------------
# 12. lower()
# ------------------------------------------------------------
# Converts all letters to lowercase.

word = "PyThOn"

print(word.lower())
# python


# ------------------------------------------------------------
# 13. upper()
# ------------------------------------------------------------
# Converts all letters to uppercase.

word = "python"

print(word.upper())
# PYTHON


# ------------------------------------------------------------
# 14. capitalize()
# ------------------------------------------------------------
# Makes the first character uppercase
# and the remaining characters lowercase.

word = "python"

print(word.capitalize())
# Python


# ------------------------------------------------------------
# 15. title()
# ------------------------------------------------------------
# Capitalizes the first character of every word.

sentence = "python is fun"

print(sentence.title())
# Python Is Fun


# ------------------------------------------------------------
# 16. strip()
# ------------------------------------------------------------
# Removes whitespace from BOTH ends.

name = "   Ansh   "

print(name.strip())
# Ansh


# strip() does NOT remove spaces between words.

name = "Ansh Mishra"

print(name.strip())
# Ansh Mishra


# ------------------------------------------------------------
# 17. lstrip()
# ------------------------------------------------------------
# Removes whitespace from the LEFT side.

name = "   Ansh"

print(name.lstrip())
# Ansh


# ------------------------------------------------------------
# 18. rstrip()
# ------------------------------------------------------------
# Removes whitespace from the RIGHT side.

name = "Ansh   "

print(name.rstrip())
# Ansh


# Remember:
#
# strip()  → both sides
# lstrip() → left side
# rstrip() → right side


# ------------------------------------------------------------
# 19. replace()
# ------------------------------------------------------------
# Replaces one part of a String with another.

text = "I like Java"

text = text.replace("Java", "Python")

print(text)
# I like Python


# replace() returns a NEW String.
# It does not modify the original String in place.


# ------------------------------------------------------------
# 20. count()
# ------------------------------------------------------------
# count() tells how many times a character
# or substring occurs.

word = "banana"

print(word.count("a"))
# 3


text = "hello hello"

print(text.count("hello"))
# 2


# ------------------------------------------------------------
# 21. find()
# ------------------------------------------------------------
# find() returns the index of the FIRST occurrence.

word = "banana"

print(word.find("a"))
# 1


# If the character/substring is not found:
# find() returns -1.

print(word.find("z"))
# -1


# Remember:
#
# count() → HOW MANY?
# find()  → WHERE is the FIRST one?


# ------------------------------------------------------------
# 22. index()
# ------------------------------------------------------------
# index() is similar to find().
# It returns the index of the FIRST occurrence.

word = "banana"

print(word.index("a"))
# 1


# IMPORTANT:
#
# find() → returns -1 if not found
# index() → raises ValueError if not found


# ------------------------------------------------------------
# 23. startswith()
# ------------------------------------------------------------
# Checks whether a String starts with a specific value.

word = "Python"

print(word.startswith("Py"))
# True

print(word.startswith("Java"))
# False


# ------------------------------------------------------------
# 24. endswith()
# ------------------------------------------------------------
# Checks whether a String ends with a specific value.

word = "Python"

print(word.endswith("on"))
# True

print(word.endswith("py"))
# False


# ------------------------------------------------------------
# 25. split()
# ------------------------------------------------------------
# split() breaks a String into a LIST.

sentence = "I love Python"

words = sentence.split()

print(words)
# ['I', 'love', 'Python']


# By default, split() separates using whitespace.


# We can specify a separator:

data = "apple,banana,mango"

fruits = data.split(",")

print(fruits)
# ['apple', 'banana', 'mango']


# Remember:
#
# split() → String → List


# ------------------------------------------------------------
# 26. join()
# ------------------------------------------------------------
# join() combines multiple Strings into ONE String.

words = ["Python", "Java", "C"]

sentence = " ".join(words)

print(sentence)
# Python Java C


# Different separators can be used:

print("-".join(words))
# Python-Java-C

print(",".join(words))
# Python,Java,C

print("".join(words))
# PythonJavaC


# Remember:
#
# join() → List → String


# ------------------------------------------------------------
# 27. isdigit()
# ------------------------------------------------------------
# Checks whether ALL characters are digits.

text = "12345"

print(text.isdigit())
# True


text = "123a"

print(text.isdigit())
# False


# ------------------------------------------------------------
# 28. isalpha()
# ------------------------------------------------------------
# Checks whether ALL characters are alphabetic.

text = "Python"

print(text.isalpha())
# True


text = "Python123"

print(text.isalpha())
# False


# ------------------------------------------------------------
# 29. isalnum()
# ------------------------------------------------------------
# Checks whether ALL characters are letters OR digits.
# Spaces and symbols are NOT allowed.

text = "Python123"

print(text.isalnum())
# True


text = "Python 123"

print(text.isalnum())
# False


# Remember:
#
# isdigit() → only digits
# isalpha() → only letters
# isalnum() → letters + digits


# ------------------------------------------------------------
# 30. isspace()
# ------------------------------------------------------------
# Checks whether ALL characters are whitespace.

text = "   "

print(text.isspace())
# True


text = "Hello"

print(text.isspace())
# False


# ------------------------------------------------------------
# 31. swapcase()
# ------------------------------------------------------------
# Converts uppercase characters to lowercase
# and lowercase characters to uppercase.

text = "PyThOn"

print(text.swapcase())
# pYtHoN


# ------------------------------------------------------------
# 32. center()
# ------------------------------------------------------------
# Places the String in the center of a given width.

word = "Python"

print(word.center(10))


# A character can also be used for padding:

print(word.center(10, "-"))

# Conceptually:
# --Python--


# ------------------------------------------------------------
# 33. format()
# ------------------------------------------------------------
# format() allows values to be inserted into a String.

name = "Ansh"
age = 20

print("My name is {} and I am {} years old".format(name, age))

# My name is Ansh and I am 20 years old


# ------------------------------------------------------------
# 34. f-STRINGS
# ------------------------------------------------------------
# f-strings are a modern and commonly used
# way to format Strings.

name = "Ansh"
age = 20

print(f"My name is {name} and I am {age} years old")

# My name is Ansh and I am 20 years old


# Expressions can also be used inside {}:

age = 20

print("Next year I will be {age + 1}")
# Next year I will be 21


# ============================================================
#                 STRING METHODS SUMMARY
# ============================================================

# lower()       → lowercase
# upper()       → uppercase
# capitalize()  → first character uppercase
# title()       → first letter of every word uppercase
#
# strip()       → remove whitespace from both sides
# lstrip()      → remove left whitespace
# rstrip()      → remove right whitespace
#
# replace()     → replace part of a String
# count()       → count occurrences
# find()        → first index, -1 if not found
# index()       → first index, error if not found
#
# startswith()  → check beginning
# endswith()    → check ending
#
# split()       → String → List
# join()        → List → String
#
# isdigit()     → only digits
# isalpha()     → only letters
# isalnum()     → letters + digits
# isspace()     → only whitespace
#
# swapcase()    → switch upper/lower case
# center()      → center String
#
# format()      → String formatting
# f-string      → modern String formatting


# ============================================================
#                  STRING MENTAL MODEL
# ============================================================

# String:
#
# → ordered
# → indexed
# → supports negative indexing
# → supports slicing
# → immutable
# → supports loops
# → supports membership checking
#
#
# IMPORTANT:
#
# String is a SEQUENCE OF CHARACTERS.
#
# Example:
#
# word = "Python"
#
# P  y  t  h  o  n
# 0  1  2  3  4  5
#
# -6 -5 -4 -3 -2 -1


# ============================================================
#                 IMPORTANT COMPARISONS
# ============================================================

# count()
# → How many times?


# find()
# → Where is the FIRST occurrence?
# → -1 if not found


# index()
# → Where is the FIRST occurrence?
# → Error if not found


# split()
# → String becomes List


# join()
# → List of Strings becomes String


# ============================================================
#                       END OF NOTES
# ============================================================