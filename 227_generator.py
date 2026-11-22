# GENERATOR PRACTICE 2

# Create a generator function called countdown().

# It should generate numbers from 10 down to 1.

# Use a for loop and range() inside the generator.

# Use another for loop outside the function to print the values.
def countdown():
    for num in range(10, 0, -1):
        yield num

for value in countdown():
    print(value)
