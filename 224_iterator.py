# ITERATOR PRACTICE 3

# Create a list containing: [15, 25, 35, 45, 55]

# Convert the list into an iterator.

# Print the first two elements using next().

# Then use a while loop with try-except StopIteration
# to print all the remaining elements.

# Make sure you don't print the first two elements again.

list = [15, 25, 35, 45, 55]
iterator = iter(list)
print(next(iterator))
print(next(iterator))

while True :
    try:
        print(next(iterator))
    except StopIteration:
        break
