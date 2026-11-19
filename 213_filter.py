# QUESTION 3: Filter Names with 5 or More Characters
#
# You are given a list of names.
#
# Your task:
# 1. Use filter() and lambda.
# 2. Keep only names whose length is 5 or more.
# 3. Store the filtered result in a new list.
# 4. Print the final list.
#
# Input:
# names = ["Ansh", "Rahul", "Aman", "Priya", "Rohit", "Raj"]
#
# Expected Output:
# ["Rahul", "Priya", "Rohit"]

names = ["Ansh", "Rahul", "Aman", "Priya", "Rohit", "Raj"]
result = filter(lambda n: len(n) >= 5, names)
print(list(result))