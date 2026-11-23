# ============================================================
# GENERATOR EXPRESSION PRACTICE 1
# ============================================================
#
# Given:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# 1. Create a generator expression that generates
#    the cubes of all numbers in the list.
#
# 2. Store the generator expression in a variable
#    called cubes.
#
# 3. Use a for loop to print every generated value.
#
# Expected output:
# 1
# 8
# 27
# 64
# 125
# 216
# 343
# 512
# 729
# 1000
#
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cube = (num ** 3 for num in numbers)
for value in cube:
    print(value)

