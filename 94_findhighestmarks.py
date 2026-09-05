# Problem 4: Find Highest Marks
#
# Write a function:
# highest_marks(students)
#
# - takes a dictionary containing student names and marks.
# - finds the highest marks.
# - returns the highest marks.
#
# Example:
# highest_marks({
#     "Ansh": 85,
#     "Rahul": 90,
#     "Aman": 78,
#     "Riya": 95
# })
# should return 95
def highest_marks(students):
    highest = list(students.values())[0]

    for marks in students.values():
      if marks > highest:
        highest = marks
    return highest
print(highest_marks({
     "Ansh": 85,
     "Rahul": 90,
     "Aman": 78,
     "Riya": 95
     }))