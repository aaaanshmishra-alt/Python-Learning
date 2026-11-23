# ============================================================
# GENERATOR EXPRESSION PRACTICE 2
# ============================================================
#
# Given:
# numbers = [12, 7, 25, 40, 9, 60, 15, 80, 3, 100]
#
# 1. Create a generator expression called multiples.
# 2. Generate only numbers divisible by 5.
# 3. Use a for loop to print the generated values.
#
# Expected output:
# 25
# 40
# 60
# 15
# 80
# 100
#
# ============================================================

numbers = [12, 7, 25, 40, 9, 60, 15, 80, 3, 100]
multiplies = (num for num in numbers if num % 5 == 0 )
for values in multiplies:
    print(values)

