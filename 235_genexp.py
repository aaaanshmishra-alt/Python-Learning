# ============================================================
# GENERATOR EXPRESSION PRACTICE 4
# ============================================================
#
# Given:
# numbers = [2, 5, 8, 11, 14, 17, 20]
#
# 1. Use a generator expression.
# 2. Generate the squares of only the even numbers.
# 3. Pass the generator expression directly into sum().
# 4. Store the result in a variable called total.
# 5. Print total.
#
# Expected output:
# 984
#
# ============================================================

numbers = [2, 5, 8, 11, 14, 17, 20]

total = sum(num ** 2 for num in numbers if num % 2 == 0 )
print(total)