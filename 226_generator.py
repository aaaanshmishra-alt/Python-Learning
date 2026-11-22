# GENERATOR PRACTICE 1

# Create a generator function called even_numbers().

# Use a for loop and range() inside the generator.

# The generator should produce even numbers from 2 to 20.

# Use another for loop outside the generator function
# to print all the generated numbers.

def even_numbers():
    for num in range(2, 21, 2):
        yield num

for value in even_numbers():
    print(value)


    