# Problem 19: Most Common Vowel
#
# Write a function:
# most_common_vowel(text)
#
# - takes a string.
# - finds the vowel that appears the most times.
# - ignores uppercase/lowercase differences.
# - returns the vowel in lowercase.
# - if there are no vowels, return -1.
#
# Example:
# most_common_vowel("Programming is Awesome")
# should return "o"
#
# most_common_vowel("rhythm")
# should return -1
def most_common_vowel(text):
    common_vowel = 0
    top_character = ""

    for character in text:
        count = text.lower().count(character.lower())

        if character.lower() in "aeiou":
            if count > common_vowel:
                common_vowel = count
                top_character = character.lower()

    if common_vowel == 0:
        return -1

    return top_character


print(most_common_vowel("Programming is Awesome"))
print(most_common_vowel("rhythm"))

        
       

