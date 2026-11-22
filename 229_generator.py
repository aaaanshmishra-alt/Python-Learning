# ============================================================
# GENERATOR PRACTICE 4
# ============================================================
#
# Create a generator function called squares().
#
# Given:
# numbers = [2, 3, 4, 5, 6]
#
# Requirements:
# 1. Use a for loop inside the generator.
# 2. Calculate the square of each number.
# 3. Yield the squared value.
# 4. Use a for loop outside the generator to print
#    each generated value.
#
# Expected output:
# 4
# 9
# 16
# 25
# 36
#
# ============================================================
numbers = [2, 3, 4, 5, 6]
def squares():
    for num in numbers:
         
        yield num * num
for value in squares():
    print(value)



