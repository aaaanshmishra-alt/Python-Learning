# ============================================================
# PHASE 4 — LAMBDA FUNCTIONS
# QUESTION 3: SORT WORDS BY LENGTH
# ============================================================
#
# PROBLEM STATEMENT:
#
# You are given the following list:
#
# words = ["python", "AI", "programming", "code", "developer"]
#
# REQUIREMENTS:
#
# 1. Use sorted() to sort the words by their length.
#
# 2. Use a lambda function with the key parameter.
#
# 3. Store the sorted list in a variable named result.
#
# 4. Print result.
#
# EXPECTED OUTPUT:
#
# ['AI', 'code', 'python', 'developer', 'programming']
#
# RULES:
#
# - Use lambda, not def.
# - Use len() to calculate each word's length.
# - Do not manually rearrange the words.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
words = ["python", "AI", "programming", "code", "developer"]
result = sorted(words, key=lambda words : len(words))
print(result)