# Problem 12: Remove Duplicate Characters
#
# Write a function:
# remove_duplicates(text)
#
# - takes a string.
# - removes repeated characters.
# - keeps the FIRST occurrence of each character.
# - returns the resulting string.
#
# Example:
# remove_duplicates("banana")
# should return "ban"
#
# remove_duplicates("programming")
# should return "progamin"
def remove_duplicates(text):
    result = ""
    seen = set()

    for character in text:
        if character not in seen:
            result = result + character
            seen.add(character)

    return result

print(remove_duplicates("programming"))