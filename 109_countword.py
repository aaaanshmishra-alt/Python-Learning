# Problem 5: Count Words
#
# Write a function:
# count_words(sentence)
#
# - takes a string containing a sentence.
# - returns the number of words in the sentence.
#
# Example:
# count_words("I love Python")
# should return 3
#
# count_words("Python is very easy")
# should return 4
def count_words(sentence):
    words = sentence.split()
    return len(words)
print(count_words("Python is very easy"))

