# Problem 17: Find the Longest Word
#
# Write a function:
# longest_word(sentence)
#
# - takes a sentence.
# - finds the longest word.
# - returns that word.
#
# Example:
# longest_word("I love programming")
# should return "programming"
#
# longest_word("Python is very powerful")
# should return "powerful"
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(longest_word("Python is very powerful"))
    