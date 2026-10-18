# ============================================================
# ADVANCED FUNCTIONS — DEFAULT ARGUMENTS
# ============================================================

# A default argument is a parameter that already has a
# default value.
#
# If the user does not provide a value for that parameter,
# Python automatically uses the default value.


# ------------------------------------------------------------
# 1. BASIC DEFAULT ARGUMENT
# ------------------------------------------------------------

def greet(name="Ansh"):
    print("Hello", name)

greet()

# Output:
# Hello Ansh


# If we provide a value:

greet("Rahul")

# Output:
# Hello Rahul


# ------------------------------------------------------------
# 2. HOW IT WORKS
# ------------------------------------------------------------

def greet(name="Ansh"):
    print("Hello", name)

# No argument:
greet()

# Python uses:
# name = "Ansh"


# Argument provided:
greet("Rohit")

# Python uses:
# name = "Rohit"


# ------------------------------------------------------------
# 3. DEFAULT VALUE WITH NORMAL PARAMETER
# ------------------------------------------------------------

def power(number, exponent=2):
    return number ** exponent

print(power(5))

# Output:
# 25

# Because exponent was not provided,
# Python uses the default value:
#
# exponent = 2


# We can also provide the exponent:

print(power(5, 3))

# Output:
# 125


# ------------------------------------------------------------
# 4. MULTIPLE DEFAULT PARAMETERS
# ------------------------------------------------------------

def introduce(name, age=18, city="Bangalore"):
    print(name, age, city)

introduce("Ansh")

# Output:
# Ansh 18 Bangalore


introduce("Rahul", 20, "Delhi")

# Output:
# Rahul 20 Delhi


# ============================================================
# QUICK MEMORY
# ============================================================

# Normal parameter:
# def function(name):

# Default parameter:
# def function(name="Ansh"):

# If argument is NOT provided:
# → default value is used
#
# If argument IS provided:
# → provided value is used
# ============================================================