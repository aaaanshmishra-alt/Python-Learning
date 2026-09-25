# Problem Statement — Shopping Cart Analyzer
#
# Write a Python program to create a Shopping Cart Analyzer.
#
# The program should:
#
# 1. Take the names and prices of 6 products as input.
#
# 2. Store the product names and prices in a dictionary.
#
# 3. Display all products with their prices.
#
# 4. Calculate and display the total cost of all products.
#
# 5. Calculate and display the average price of the products.
#
# 6. Find the most expensive product without using max().
#
# 7. Find the cheapest product without using min().
#
# 8. Create a dictionary comprehension containing products
#    whose price is greater than 500.
#
# 9. Create a list comprehension containing the names of
#    products whose price is below 200.
#
# 10. Apply a 10% discount to products costing more than 1000
#     and display their discounted prices.
#
# Restrictions:
#
# - Do not use max() or min().
# - Use loops and conditional statements.
# - Use dictionary comprehension and list comprehension
#   where requested.
# - Do not use external libraries.
#
# Topics:
# Input, dictionaries, loops, conditions, arithmetic operators,
# dictionary comprehension, list comprehension, and output formatting.
products = {}

for i in range(6):
    name = input(f"Enter product {i + 1} name: ")
    price = float(input(f"Enter price of {name}: "))
    products[name] = price


print("\nShopping Cart")

for name, price in products.items():
    print(f"{name}: ₹{price:.2f}")


total = 0

for price in products.values():
    total += price

average = total / len(products)


expensive_name = ""
expensive_price = -1

cheap_name = ""
cheap_price = float("inf")

for name, price in products.items():

    if price > expensive_price:
        expensive_price = price
        expensive_name = name

    if price < cheap_price:
        cheap_price = price
        cheap_name = name


above_500 = {
    name: price
    for name, price in products.items()
    if price > 500
}


below_200 = [
    name
    for name, price in products.items()
    if price < 200
]


discounted_products = {}

for name, price in products.items():

    if price > 1000:
        discounted_price = price * 0.90
        discounted_products[name] = discounted_price


print(f"\nTotal Cost: ₹{total:.2f}")
print(f"Average Price: ₹{average:.2f}")

print(f"\nMost Expensive Product: {expensive_name} - ₹{expensive_price:.2f}")
print(f"Cheapest Product: {cheap_name} - ₹{cheap_price:.2f}")

print(f"\nProducts Above ₹500: {above_500}")

print(f"Products Below ₹200: {below_200}")

print("\nProducts After 10% Discount:")

for name, price in discounted_products.items():
    print(f"{name}: ₹{price:.2f}")