# ============================================================
# GENERATOR EXPRESSION PRACTICE 3
# ============================================================
#
# Given:
# numbers = [5, 10, 15, 20, 25]
#
# 1. Use a generator expression directly inside sum().
#
# 2. Generate the cubes of all numbers.
#
# 3. Calculate the total of all generated cubes.
#
# 4. Store the result in a variable called total.
#
# 5. Print total.
#
# Expected output:
#  28125
#
# ============================================================
numbers = [5, 10, 15, 20, 25]
total = sum(num ** 3 for num in numbers)
print(total)
