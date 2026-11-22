# GENERATOR PRACTICE 3

# Create a generator function called positive_numbers().

# Given the list:
# numbers = [-5, 10, -2, 15, 0, 20, -8, 25]

# Use a for loop inside the generator.

# Use an if condition to check whether a number is positive.

# Yield only positive numbers.
# Use another for loop outside the generator function
# to print the generated values.
numbers = [-5, 10, -2, 15, 0, 20, -8, 25]

def positive_numbers():
    for num in numbers:
        if num > 0:
            yield num

for value in positive_numbers():
    print(value)
    

     

