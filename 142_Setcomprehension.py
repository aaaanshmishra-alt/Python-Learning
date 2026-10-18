# ============================================================
# SET COMPREHENSION
# ============================================================

# Set comprehension is a short way to create a SET
# using a loop.
#
# It works similarly to list comprehension and
# dictionary comprehension.


# ------------------------------------------------------------
# 1. BASIC SET COMPREHENSION
# ------------------------------------------------------------

# Normal approach:

numbers = [1, 2, 3, 4, 5]

squares = set()

for number in numbers:
    squares.add(number * number)

print(squares)

# Output:
# {1, 4, 9, 16, 25}


# Using set comprehension:

squares = {number * number for number in numbers}

print(squares)

# Output:
# {1, 4, 9, 16, 25}


# Basic syntax:
#
# {expression for item in collection}


# ------------------------------------------------------------
# 2. SET COMPREHENSION AUTOMATICALLY REMOVES DUPLICATES
# ------------------------------------------------------------

numbers = [1, 2, 2, 3, 3, 3, 4]

result = {x for x in numbers}

print(result)

# Output:
# {1, 2, 3, 4}

# Sets automatically store only UNIQUE values.


# ------------------------------------------------------------
# 3. SET COMPREHENSION WITH TRANSFORMATION
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

result = {x * 2 for x in numbers}

print(result)

# Output:
# {2, 4, 6, 8, 10}


# ------------------------------------------------------------
# 4. SET COMPREHENSION WITH IF
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

result = {x for x in numbers if x % 2 == 0}

print(result)

# Output:
# {2, 4, 6}


# Syntax:
#
# {expression for item in collection if condition}


# ------------------------------------------------------------
# 5. FILTER + TRANSFORM
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

result = {x * x for x in numbers if x % 2 == 0}

print(result)

# Output:
# {4, 16, 36}

# First:
#   if x % 2 == 0
#   → select even numbers
#
# Then:
#   x * x
#   → square them
#
# Because this is a SET, duplicate results would
# automatically be removed.


# ------------------------------------------------------------
# 6. LIST vs SET vs DICTIONARY COMPREHENSION
# ------------------------------------------------------------

numbers = [1, 2, 3]

# List:
result = [x * x for x in numbers]

# Output:
# [1, 4, 9]


# Set:
result = {x * x for x in numbers}

# Output:
# {1, 4, 9}


# Dictionary:
result = {x: x * x for x in numbers}

# Output:
# {1: 1, 2: 4, 3: 9}


# ============================================================
# QUICK MEMORY
# ============================================================

# LIST:
# [expression for item in collection]

# SET:
# {expression for item in collection}

# DICTIONARY:
# {key: value for item in collection}


# Remember:
#
# LIST       → [ ]
# SET        → { }
# DICTIONARY → {key: value}
#
# SET → unique values
# DICTIONARY → key : value pairs
# ============================================================