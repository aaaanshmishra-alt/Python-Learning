# MODULE 1 — QUESTION 6
#
# Write a Python program that:
#
# 1. Accepts the radius of a circle from the user.
# 2. Calculates the area of the circle.
# 3. Calculates the circumference of the circle.
# 4. Use the math module and math.pi.
# 5. Display both results using f-string formatting.
#
# Formula:
# Area = π × r × r
# Circumference = 2 × π × r
#
# Write the complete program below.
import math
radius = int(input("Enter the number = "))
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"The area of the circle is {area} and the circumference is {circumference}")