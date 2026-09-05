# Problem 18: Second Longest Word
#
# Write a function:
# second_longest_word(sentence)
#
# - takes a sentence.
# - finds the second longest word.
# - returns that word.
#
# Example:
# second_longest_word("I love Python programming")
# should return "Python"
#
# second_longest_word("Java is very powerful")
# should return "powerful"
def second_longest_word(sentence):
    words = sentence.split()

    longest = ""
    second_longest = ""

    for word in words:
        if len(word) > len(longest):
            second_longest = longest
            longest = word

        elif len(word) > len(second_longest):
            second_longest = word

    return second_longest
print(second_longest_word("Java is very powerful"))
     