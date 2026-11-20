# ITERATOR PRACTICE 1

# Create a list containing the numbers 10, 20, 30 and 40.

# Convert the list into an iterator using iter().

# Use next() three times to print the first three elements.

# Then use next() with a default value of "No more elements"
# to print the next element.

# Finally, call next() once more using the same default value
# and print the result.
numbers = [10, 20, 30, 40]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

print(next(iterator, "No more elements"))
print(next(iterator, "No more elements"))