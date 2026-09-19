# ============================================================
# PRACTICE PROBLEM 3 — TRANSFORM VALUES
# ============================================================

# Problem:
# Given a list of numbers, create a dictionary where:
#
# - Each number is the KEY.
# - If the number is even, its VALUE should be "Even".
# - If the number is odd, its VALUE should be "Odd".
#
# Input:
# numbers = [1, 2, 3, 4, 5]
#
# Expected Output:
# {1: "Odd", 2: "Even", 3: "Odd", 4: "Even", 5: "Odd"}
#
# Hint:
# This time you need IF-ELSE because every number must
# appear in the dictionary.
#
# Structure:
# {key: A if condition else B for item in collection}
#
# Write your solution below:
# ============================================================

numbers = [1, 2, 3, 4, 5]
result = {x : "Even" if x % 2 == 0 else "Odd" for x in numbers}
print(result)