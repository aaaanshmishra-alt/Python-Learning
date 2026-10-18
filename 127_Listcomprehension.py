# ============================================================
# LIST COMPREHENSION
# ============================================================

# List comprehension is a shorter way of creating a new list
# using a loop.

# ------------------------------------------------------------
# 1. BASIC LIST COMPREHENSION
# ------------------------------------------------------------

# Normal for loop:

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)

# Using list comprehension:

squares = [number * number for number in numbers]

# Basic syntax:
# [expression for item in collection]


# ------------------------------------------------------------
# 2. LIST COMPREHENSION WITH FILTERING
# ------------------------------------------------------------

# We can use an if condition to select only certain items.

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

# Output:
# [2, 4, 6]

# Syntax:
# [expression for item in collection if condition]

# The if at the END acts as a FILTER.
# Items that don't satisfy the condition are not added.


# ------------------------------------------------------------
# 3. FILTER + TRANSFORM
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

result = [number * 2 for number in numbers if number % 2 == 0]

# Output:
# [4, 8, 12]

# First:
#   if number % 2 == 0
#   → select even numbers
#
# Then:
#   number * 2
#   → transform those numbers


# ------------------------------------------------------------
# 4. IF-ELSE IN LIST COMPREHENSION
# ------------------------------------------------------------

# We can give a different output depending on a condition.

numbers = [1, 2, 3, 4, 5]

result = ["Even" if number % 2 == 0 else "Odd"
          for number in numbers]

# Output:
# ["Odd", "Even", "Odd", "Even", "Odd"]

# Syntax:
# [value_if_true if condition else value_if_false
#  for item in collection]

# IMPORTANT:
#
# Filter:
# [x for x in numbers if condition]
#
# IF-ELSE:
# [A if condition else B for x in numbers]
#
# Filter removes items.
# If-else gives EVERY item an output.


# ------------------------------------------------------------
# 5. IF-ELSE WITH CALCULATION
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

result = [x * 2 if x % 2 == 0 else x * 3
          for x in numbers]

# Output:
# [3, 4, 9, 8, 15, 12]

# Even → multiply by 2
# Odd  → multiply by 3


# ============================================================
# QUICK MEMORY
# ============================================================

# Basic:
# [expression for item in collection]

# Filter:
# [expression for item in collection if condition]

# If-else:
# [A if condition else B for item in collection]

# Think:
# FILTER → TRANSFORM → BUILD LIST
# ============================================================