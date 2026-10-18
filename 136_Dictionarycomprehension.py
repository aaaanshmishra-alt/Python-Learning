# ============================================================
# DICTIONARY COMPREHENSION
# ============================================================

# Dictionary comprehension is a shorter way to create a
# dictionary using a loop.
#
# It works similarly to list comprehension, but instead of
# producing individual values, it produces KEY: VALUE pairs.


# ------------------------------------------------------------
# 1. BASIC DICTIONARY COMPREHENSION
# ------------------------------------------------------------

# Normal approach:

numbers = [1, 2, 3, 4, 5]

squares = {}

for number in numbers:
    squares[number] = number * number

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Using dictionary comprehension:

squares = {number: number * number for number in numbers}

print(squares)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Basic syntax:
#
# {key: value for item in collection}


# ------------------------------------------------------------
# 2. UNDERSTANDING KEY AND VALUE
# ------------------------------------------------------------

numbers = [2, 3, 4]

result = {x: x * x for x in numbers}

# For x = 2:
# key   = 2
# value = 4
#
# For x = 3:
# key   = 3
# value = 9
#
# For x = 4:
# key   = 4
# value = 16
#
# Result:
# {2: 4, 3: 9, 4: 16}


# ------------------------------------------------------------
# 3. DICTIONARY COMPREHENSION WITH CALCULATION
# ------------------------------------------------------------

numbers = [1, 2, 3, 4]

result = {x: x * 10 for x in numbers}

# Output:
# {1: 10, 2: 20, 3: 30, 4: 40}


# ------------------------------------------------------------
# 4. DICTIONARY COMPREHENSION WITH IF
# ------------------------------------------------------------

# We can use an if condition to FILTER which items
# should be included in the dictionary.

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    x: x * x
    for x in numbers
    if x % 2 == 0
}

print(even_squares)

# Output:
# {2: 4, 4: 16, 6: 36}


# Syntax:
#
# {key: value for item in collection if condition}


# ------------------------------------------------------------
# 5. FILTER + TRANSFORM
# ------------------------------------------------------------

# Dictionary comprehension can perform two operations:
#
# 1. FILTER → decide which items to keep
# 2. TRANSFORM → decide what value to store


numbers = [1, 2, 3, 4, 5, 6]

result = {
    x: x * 2
    for x in numbers
    if x % 2 == 0
}

# First, select even numbers:
# 2, 4, 6
#
# Then multiply each by 2:
# 4, 8, 12
#
# Final dictionary:
# {2: 4, 4: 8, 6: 12}


# ------------------------------------------------------------
# 6. DIFFERENCE BETWEEN LIST AND DICTIONARY COMPREHENSION
# ------------------------------------------------------------

# List comprehension:

numbers = [1, 2, 3]

result = [x * x for x in numbers]

# Output:
# [1, 4, 9]


# Dictionary comprehension:

result = {x: x * x for x in numbers}

# Output:
# {1: 1, 2: 4, 3: 9}


# List:
# [expression for item in collection]
#
# Dictionary:
# {key: value for item in collection}


# ============================================================
# QUICK MEMORY
# ============================================================

# BASIC:
# {key: value for item in collection}

# WITH FILTER:
# {key: value for item in collection if condition}

# Remember:
#
# LIST  → values
# DICT  → key : value
#
# Dictionary comprehension always creates a dictionary
# containing KEY: VALUE pairs.
# ============================================================