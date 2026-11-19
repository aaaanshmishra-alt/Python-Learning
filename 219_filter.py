# QUESTION 9: Filter Students Who Scored 80 or More
#
# You are given a list of dictionaries containing student names and marks.
#
# Your task:
# 1. Use filter() and lambda.
# 2. Keep only students whose marks are 80 or more.
# 3. Store the filtered result in a new list.
# 4. Print the final list.
#
# Input:
# students = [
#     {"name": "Ansh", "marks": 92},
#     {"name": "Rahul", "marks": 67},
#     {"name": "Aman", "marks": 85},
#     {"name": "Priya", "marks": 76},
#     {"name": "Rohit", "marks": 88}
# ]
#
# Expected Output:
# [
#     {"name": "Ansh", "marks": 92},
#     {"name": "Aman", "marks": 85},
#     {"name": "Rohit", "marks": 88}
# ]

students = [
     {"name": "Ansh", "marks": 92},
     {"name": "Rahul", "marks": 67},
     {"name": "Aman", "marks": 85},
     {"name": "Priya", "marks": 76},
  {"name": "Rohit", "marks": 88} 
  ]
result = filter(lambda n : n["marks"] >= 80, students)
print(list(result))