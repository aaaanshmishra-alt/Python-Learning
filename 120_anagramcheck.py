# Problem 16: Check Anagram
#
# Write a function:
# is_anagram(first, second)
#
# - takes two strings.
# - returns True if they are anagrams.
# - otherwise returns False.
#
# Example:
# is_anagram("listen", "silent")
# → True
#
# is_anagram("hello", "world")
# → False

def is_anagram(first, second):
    if len(first) != len(second):
        return False

    for character in first:
        if first.count(character) != second.count(character):
            return False
    return True
print(is_anagram("hello", "world"))
