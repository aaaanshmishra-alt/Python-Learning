# ============================================================
# PRACTICE PROBLEM 2 — DEFAULT ARGUMENT
# ============================================================

# Problem:
# Create a function called `greet_user`.
#
# The function should take:
# - name
# - greeting, with a DEFAULT value of "Hello"
#
# The function should return:
# greeting + " " + name
#
# Examples:
#
# greet_user("Ansh")
# → "Hello Ansh"
#
# greet_user("Ansh", "Welcome")
# → "Welcome Ansh"
#
# Hint:
# The default value should be assigned while defining
# the function.
#
# Write your solution below:
# ============================================================
def greet_user(name, greeting = "Hello"):
    return greeting + " " + name
print(greet_user("Ansh"))
print(greet_user("Ansh", "Welcome"))