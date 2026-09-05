# ============================================================
#                        PYTHON TUPLES
# ============================================================


# ------------------------------------------------------------
# 1. WHAT IS A TUPLE?
# ------------------------------------------------------------
# A tuple is a collection used to store multiple values
# together.
#
# Tuples are similar to Lists, but the major difference is:
#
# List   → Mutable
# Tuple  → Immutable
#
# Tuples are generally written using parentheses ().

numbers = (10, 20, 30, 40)

print(numbers)
# (10, 20, 30, 40)


# ------------------------------------------------------------
# 2. TUPLE CAN STORE DIFFERENT DATA TYPES
# ------------------------------------------------------------
# A tuple can contain different types of values.

student = ("Ansh", 19, 8.5, True)

print(student)


# ------------------------------------------------------------
# 3. TUPLE INDEXING
# ------------------------------------------------------------
# Tuple indexing works exactly like List indexing.
#
# Python indexing starts from 0.

numbers = (10, 20, 30, 40)

print(numbers[0])
# 10

print(numbers[2])
# 30


# ------------------------------------------------------------
# 4. NEGATIVE INDEXING
# ------------------------------------------------------------
# Negative indexes allow us to access elements from the end.
#
# -1 → last element
# -2 → second-last element
# -3 → third-last element

numbers = (10, 20, 30, 40)

print(numbers[-1])
# 40

print(numbers[-2])
# 30


# ------------------------------------------------------------
# 5. TUPLES ARE IMMUTABLE
# ------------------------------------------------------------
# Immutable means that once a tuple is created,
# its elements cannot be changed.

numbers = (10, 20, 30)

# numbers[0] = 99
#
# This will give a TypeError.


# ------------------------------------------------------------
# 6. LIST VS TUPLE
# ------------------------------------------------------------
# List → Mutable
# Tuple → Immutable

numbers_list = [10, 20, 30]

numbers_list[0] = 99

print(numbers_list)
# [99, 20, 30]


numbers_tuple = (10, 20, 30)

# numbers_tuple[0] = 99
#
# Error because tuples cannot be modified.


# ------------------------------------------------------------
# 7. TUPLE UNPACKING
# ------------------------------------------------------------
# Tuple unpacking means taking values from a tuple
# and assigning them to separate variables.

student = ("Ansh", 19, "CSE")

name, age, branch = student

print(name)
# Ansh

print(age)
# 19

print(branch)
# CSE


# ------------------------------------------------------------
# 8. TUPLE SLICING
# ------------------------------------------------------------
# Tuples support slicing just like Lists.
#
# Syntax:
# tuple[start:stop]
#
# start → included
# stop  → NOT included

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
# (20, 30, 40)


# ------------------------------------------------------------
# 9. SLICING FROM THE BEGINNING
# ------------------------------------------------------------
# If start is omitted, slicing starts from index 0.

numbers = (10, 20, 30, 40, 50)

print(numbers[:3])
# (10, 20, 30)


# ------------------------------------------------------------
# 10. SLICING UNTIL THE END
# ------------------------------------------------------------
# If stop is omitted, slicing continues until the end.

numbers = (10, 20, 30, 40, 50)

print(numbers[2:])
# (30, 40, 50)


# ------------------------------------------------------------
# 11. SLICING WITH STEP
# ------------------------------------------------------------
# Syntax:
# tuple[start:stop:step]
#
# step tells Python how many positions to move.

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[0:6:2])
# (10, 30, 50)


# ------------------------------------------------------------
# 12. TUPLE COUNT()
# ------------------------------------------------------------
# count() tells us how many times a value appears
# in the tuple.

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
# 3


# ------------------------------------------------------------
# 13. TUPLE INDEX()
# ------------------------------------------------------------
# index() returns the index of the FIRST occurrence
# of a value.

numbers = (10, 20, 30, 20, 40)

print(numbers.index(20))
# 1
#
# The first 20 is at index 1.


# ------------------------------------------------------------
# 14. TUPLE PACKING
# ------------------------------------------------------------
# We can create a tuple without explicitly using
# parentheses.
#
# Multiple values separated by commas are automatically
# packed into a tuple.

numbers = 10, 20, 30, 40

print(numbers)
# (10, 20, 30, 40)


student = "Ansh", 19, "CSE"

print(student)
# ("Ansh", 19, "CSE")


# ------------------------------------------------------------
# 15. TUPLE UNPACKING
# ------------------------------------------------------------
# Unpacking is the opposite of packing.
#
# Values from a tuple are assigned to separate variables.

person = ("Rahul", 20, "Bangalore")

name, age, city = person

print(name)
# Rahul

print(age)
# 20

print(city)
# Bangalore


# ------------------------------------------------------------
# 16. SINGLE-ELEMENT TUPLE
# ------------------------------------------------------------
# A single value inside parentheses is NOT automatically
# a tuple.
#
# The comma is what makes it a tuple.

x = (10)

print(type(x))
# int


# Correct way to create a one-element tuple:

x = (10,)

print(type(x))
# tuple


# Remember:
#
# (10)  → integer
# (10,) → tuple


# ------------------------------------------------------------
# 17. LOOPING THROUGH A TUPLE
# ------------------------------------------------------------
# We can loop through a tuple just like a List.

numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)

# Output:
# 10
# 20
# 30
# 40


# ------------------------------------------------------------
# 18. LOOPING USING INDEXES
# ------------------------------------------------------------
# We can also loop through the indexes of a tuple
# using range() and len().

numbers = (10, 20, 30)

for i in range(len(numbers)):
    print(numbers[i])

# Output:
# 10
# 20
# 30


# ------------------------------------------------------------
# 19. ACCESSING VALUES USING INDEXES IN A LOOP
# ------------------------------------------------------------
# i represents the index.
# numbers[i] gives the value at that index.

numbers = (5, 10, 15)

for i in range(len(numbers)):
    print(numbers[i])

# Output:
# 5
# 10
# 15


# ============================================================
#                    IMPORTANT SUMMARY
# ============================================================

# tuple = (10, 20, 30)
#       → create a tuple

# tuple[index]
#       → access an element

# tuple[-1]
#       → access the last element

# tuple[start:stop]
#       → slice a tuple

# tuple[start:stop:step]
#       → slice with a step

# tuple.count(value)
#       → count how many times a value occurs

# tuple.index(value)
#       → find the index of the FIRST occurrence

# name, age = person
#       → tuple unpacking

# a = 10, 20, 30
#       → tuple packing

# (10,)
#       → one-element tuple

# for value in tuple:
#       → loop through tuple values

# for i in range(len(tuple)):
#       → loop through tuple indexes


# ============================================================
#                  MOST IMPORTANT DIFFERENCE
# ============================================================

# LIST:
# numbers = [10, 20, 30]
# numbers[0] = 99
# → Allowed because Lists are MUTABLE.


# TUPLE:
# numbers = (10, 20, 30)
# numbers[0] = 99
# → NOT allowed because Tuples are IMMUTABLE.


# Remember:
#
# LIST  → Mutable
# TUPLE → Immutable
#
# Both support:
# → Indexing
# → Negative indexing
# → Slicing
# → Loops
# → len()
# → in / not in
#
# But Tuples cannot be modified after creation.