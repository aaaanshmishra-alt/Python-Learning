# Problem 13: Check Palindrome
#
# Write a function:
# is_palindrome(text)
#
# - takes a string.
# - returns True if the string reads the same
#   forward and backward.
# - otherwise returns False.
#
# Example:
# is_palindrome("madam")
# should return True
#
# is_palindrome("hello")
# should return False
def is_palindrome(text):
    result = ""
    for character in text:
        result = character + result
    if  text == result:
        return True
    return False
print(is_palindrome("madam"))
