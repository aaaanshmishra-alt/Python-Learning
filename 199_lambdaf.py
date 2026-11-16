# ============================================================
# PHASE 4 — LAMBDA FUNCTIONS
# QUESTION 7: CALCULATE DISCOUNTED PRICE
# ============================================================
#
# PROBLEM STATEMENT:
#
# Create a lambda function named final_price.
#
# REQUIREMENTS:
#
# 1. Accept two arguments:
#    - price
#    - discount (percentage)
#
# 2. Calculate the final price after applying the discount.
#
# 3. Test your lambda with:
#    - Price = 1000, Discount = 10
#    - Price = 2500, Discount = 20
#    - Price = 799, Discount = 0
#
# EXPECTED OUTPUT:
#
# 900.0
# 2000.0
# 799.0
#
# RULES:
# - Use lambda, not def.
# - Use both arguments.
# - Do not hardcode the answers.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================

final_price = lambda price , discount : price - (price * discount // 100)
print(final_price(1000, 10))
print(final_price(2500, 20))
print(final_price(799, 0))