# Problem 4: Reverse a String
#
# Write a function:
# reverse_string(text)
#
# - takes a string.
# - returns the string reversed.
#
# Example:
# reverse_string("hello")
# should return "olleh"
#
# reverse_string("Ansh")
# should return "hsnA"
def reverse_string(text):
    reverse = ""
    for character in text:
        reverse =character + reverse
    return reverse
print(reverse_string("hello"))
