# ============================================================
# PHASE 4 — LAMBDA FUNCTIONS
# QUESTION 9: EMPLOYEE BONUS CALCULATOR
# ============================================================
#
# PROBLEM STATEMENT:
#
# You are given an employee's salary and performance rating.
#
# REQUIREMENTS:
#
# 1. Create a lambda function named calculate_bonus.
#
# 2. It must accept two arguments:
#    - salary
#    - rating
#
# 3. Calculate the bonus based on the rating:
#
#    Rating >= 5  -> 20% bonus
#    Rating >= 4  -> 10% bonus
#    Rating >= 3  -> 5% bonus
#    Otherwise    -> 0% bonus
#
# 4. Return the BONUS AMOUNT, not the final salary.
#
# 5. Test with:
#
#    calculate_bonus(30000, 5)
#    calculate_bonus(30000, 4)
#    calculate_bonus(30000, 3)
#    calculate_bonus(30000, 2)
#
# EXPECTED OUTPUT:
#
# 6000.0
# 3000.0
# 1500.0
# 0.0
#
# RULES:
# - Use lambda, not def.
# - Use nested conditional expressions.
# - Do not hardcode the answers.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================

calculate_bonus = lambda salary, rating: salary * 0.20 if rating >= 5 else salary * 0.10 if rating >= 4 else salary * 0.05 if rating >= 3 else salary * 0.0

print(calculate_bonus(30000, 5))
print(calculate_bonus(30000, 4))
print(calculate_bonus(30000, 3))
print(calculate_bonus(30000, 2))
