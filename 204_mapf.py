# QUESTION 2: Apply a Price Increase Using map()
#
# You are given a list of product prices.
#
# Your task:
# 1. Use map() and lambda.
# 2. Increase every product price by 15%.
# 3. Store the updated prices in a new list.
# 4. Print the final list.
#
# Formula:
# New Price = Price + (Price * 15 / 100)
#
# Input:
# prices = [100, 250, 500, 1000, 2000]
#
# Expected Output:
# [115.0, 287.5, 575.0, 1150.0, 2300.0]

prices = [100, 250, 500, 1000, 2000]
New_prices = map(lambda n : n + (n * 15 / 100), prices)
print(list(New_prices))
