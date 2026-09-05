# Problem 14: Most Frequent Character
#
# Write a function:
# most_frequent(text)
#
# - takes a string.
# - finds the character that appears the most times.
# - returns that character.
#
# Example:
# most_frequent("banana")
# should return "a"
#
# most_frequent("programming")
# should return "r" or "g" depending on the actual counts.
def most_frequent(text):
    highest = 0
    top_character = ""
    for character in text:
        count = text.count(character)
        if count > highest:
            highest = count
            top_character = character
    return top_character
print(most_frequent("programming"))