# Problem 6: Remove All Spaces
#
# Write a function:
# remove_spaces(text)
#
# - takes a string.
# - removes ALL spaces from the string.
# - returns the new string.
#
# Example:
# remove_spaces("I love Python")
# should return "IlovePython"
#
# remove_spaces("Hello World")
# should return "HelloWorld"
def remove_spaces(text):
    return text.replace(" ", "")

print(remove_spaces("I love Python"))
