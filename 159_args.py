# ============================================================
# PRACTICE PROBLEM 4 — *ARGS
# ============================================================

# Create a function called join_words()
#
# It should accept ANY number of words and combine them
# into one string, separated by a space.
#
# Example:
#
# join_words("Python", "is", "fun")
# → "Python is fun"
#
# join_words("I", "am", "learning", "Python")
# → "I am learning Python"
#
# Use *args.
#
# Do NOT use the built-in join() method yet.
# ============================================================

def join_words(*args):
    result = ""
    for words in args:
        result = result + words + " "
    return result.strip() #the result.strip() will remove the space after python thats why we are using it
print(join_words("I", "am", "learning", "Python"))