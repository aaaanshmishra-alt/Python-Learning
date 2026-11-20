# ITERATOR PRACTICE 2

# Create a list containing: ["Python", "Java", "C", "JavaScript"]

# Convert the list into an iterator.

# Use a while loop to retrieve and print each element using next().

# Stop the loop gracefully when the iterator is exhausted.
list = ["Python", "Java", "C", "JavaScript"]
iterator = iter(list)
while True :
    try:
         print(next(iterator))
    except StopIteration:
         break
