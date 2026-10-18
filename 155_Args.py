# ============================================================
# ADVANCED FUNCTIONS — *ARGS
# ============================================================

# Normally, a function has a fixed number of parameters.

def add(a, b):
    return a + b

add(10, 20)

# This function expects exactly 2 positional arguments.


# ------------------------------------------------------------
# THE PROBLEM
# ------------------------------------------------------------

# What if we want to add 2 numbers?
# What if we want to add 5 numbers?
# What if we want to add 10 numbers?
#
# We don't want to create a different function for every
# possible number of arguments.


# ------------------------------------------------------------
# *ARGS
# ------------------------------------------------------------

# *args allows a function to accept a variable number
# of positional arguments.

def add(*args):
    print(args)


add(10, 20)
# (10, 20)

add(10, 20, 30, 40)
# (10, 20, 30, 40)

add(1, 2, 3, 4, 5, 6)
# (1, 2, 3, 4, 5, 6)


# ------------------------------------------------------------
# WHAT IS args?
# ------------------------------------------------------------

# Inside the function, args is a TUPLE.

def show(*args):
    print(type(args))
    print(args)

show(10, 20, 30)

# Output:
# <class 'tuple'>
# (10, 20, 30)


# ------------------------------------------------------------
# IMPORTANT
# ------------------------------------------------------------

# The name "args" is NOT mandatory.
#
# The * is what matters.

def show(*numbers):
    print(numbers)

show(10, 20, 30)

# Output:
# (10, 20, 30)


# But *args is the standard/common naming convention.


# ============================================================
# QUICK MEMORY
# ============================================================

# *args
#   ↓
# accepts any number of positional arguments
#
# Inside the function:
#   ↓
# arguments are stored as a TUPLE
#
# Example:
#
# def test(*args):
#     ...
#
# test(10, 20, 30)
#
# args = (10, 20, 30)
# ============================================================