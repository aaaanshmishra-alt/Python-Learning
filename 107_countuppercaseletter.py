# Problem 3: Count Uppercase Letters
#
# Write a function:
# count_uppercase(text)
#
# - takes a string.
# - counts how many uppercase letters are present.
# - returns the count.
#
# Example:
# count_uppercase("Hello WORLD")
# should return 6
#
# count_uppercase("AnSh")
# should return 2
def count_uppercase(text):
    count = 0
    for character in text:
        if character.isupper():
            count = count + 1
    return count
print(count_uppercase("AnSh"))

