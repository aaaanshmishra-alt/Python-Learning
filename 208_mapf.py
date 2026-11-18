# QUESTION 6: Extract First Names using map()
#
# You are given a list of full names.
#
# Your task:
# 1. Use map() and lambda.
# 2. Extract only the first name from every full name.
# 3. Store the results in a new list.
# 4. Print the final list.
#
# Input:
# names = ["Ansh Mishra", "Rahul Sharma", "Priya Singh",
#          "Aman Verma", "Rohit Kumar"]
#
# Expected Output:
# ['Ansh', 'Rahul', 'Priya', 'Aman', 'Rohit']
#
# Hint:
# Explore the split() string method.
names = ["Ansh Mishra", "Rahul Sharma", "Priya Singh","Aman Verma", "Rohit Kumar"]
split = map(lambda n : n.split()[0], names)
print(list(split))