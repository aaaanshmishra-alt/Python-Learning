# QUESTION 1: Temperature Converter using map()
#
# You are given a list of temperatures in Celsius.
#
# Your task:
# 1. Use map() and lambda.
# 2. Convert every temperature into Fahrenheit.
# 3. Store the result in a list.
# 4. Print the final list.
#
# Formula:
# Fahrenheit = (Celsius * 9/5) + 32
#
# Input:
# temperatures = [0, 10, 25, 37, 100]
#
# Expected Output:
# [32.0, 50.0, 77.0, 98.6, 212.0]
temperature =  [0, 10, 25, 37, 100]
Fahrenheit = map(lambda n : (n * 9/5) + 32,temperature)
print(list(Fahrenheit))