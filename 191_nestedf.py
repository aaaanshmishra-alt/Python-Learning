# ============================================================
# PHASE 4 — NESTED FUNCTIONS
# FINAL MASTERY TEST: PERSONALIZED GREETING
# ============================================================
#
# PROBLEM STATEMENT:
#
# Create a function named create_greeter() that accepts
# a parameter named name.
#
# REQUIREMENTS:
#
# 1. Inside create_greeter(), define an inner function
#    named greet().
#
# 2. The greet() function must print:
#    "Hello, <name>!"
#
#    Replace <name> with the name passed to create_greeter().
#
# 3. The outer function must return the greet function itself.
#
# 4. Create two greeting functions:
#
#    greet_ansh = create_greeter("Ansh")
#    greet_rahul = create_greeter("Rahul")
#
# 5. Call greet_ansh() and greet_rahul().
#
# EXPECTED OUTPUT:
#
# Hello, Ansh!
# Hello, Rahul!
#
# RULES:
#
# - Define both functions yourself.
# - Return the inner function without calling it.
# - Do not use global variables.
# - Do not hardcode the two final greeting messages.
#
# ============================================================
# WRITE YOUR CODE BELOW
# ============================================================
def create_greeter(name):
    def greet():
        print("Hello! ",name)
    return greet
greet_ansh = create_greeter("Ansh")
greet_rahul = create_greeter("Rahul")
greet_ansh()
greet_rahul()
