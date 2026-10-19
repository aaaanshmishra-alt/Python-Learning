# ============================================================
# PHASE 4 — NESTED FUNCTIONS
# CHALLENGE: GREETING FACTORY
# ============================================================
#
# PROBLEM STATEMENT:
#
# Create an outer function named greeting_factory().
#
# REQUIREMENTS:
#
# 1. Inside greeting_factory(), define a variable named
#    message and assign it the value "Hello, Python Learner!".
#
# 2. Define an inner function named greet().
#
# 3. Inside greet(), print the message variable.
#
# 4. The greeting_factory() function must RETURN the greet
#    function itself. Do not call greet() inside the return.
#
# 5. Store the returned function in a variable named my_greeting.
#
# 6. Call my_greeting() to display the greeting.
#
# EXPECTED OUTPUT:
#
# Hello, Python Learner!
#
# CONCEPTS TESTED:
# - Nested functions
# - Accessing an enclosing variable
# - Returning a function
# - Calling a returned function
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
def greeting_factory():
    message = "Hello, Python Learner!"
    def greet():
        print(message)

    return greet
my_greeting = greeting_factory()
my_greeting()
        
