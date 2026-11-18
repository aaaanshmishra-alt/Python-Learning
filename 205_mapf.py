# QUESTION 3: Convert Names into Uppercase using map()
#
# You are given a list of names.
#
# Your task:
# 1. Use map() to convert every name into uppercase.
# 2. Store the results in a new list.
# 3. Print the final list.
#
# Input:
# names = ["ansh", "rahul", "priya", "aman", "rohit"]
#
# Expected Output:
# ['ANSH', 'RAHUL', 'PRIYA', 'AMAN', 'ROHIT']
#
# Hint:
# You can use the upper() string method.

names = ["ansh", "rahul", "priya", "aman", "rohit"]
capital = map(lambda n: n.upper(), names)
print(list(capital))