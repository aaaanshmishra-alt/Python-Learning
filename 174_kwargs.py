# ============================================================
# ADVANCED FUNCTIONS — **KWARGS
# ============================================================

# **kwargs means:
# "Keyword Arguments"
#
# It allows a function to accept ANY number of
# keyword arguments.
#
# The keyword arguments are collected into a DICTIONARY.


# ============================================================
# 1. BASIC **KWARGS
# ============================================================

def student(**kwargs):
    print(kwargs)

student(name="Ansh", age=20)

# Output:
# {'name': 'Ansh', 'age': 20}


# ============================================================
# 2. WHAT HAPPENS INTERNALLY?
# ============================================================

# When we write:

student(name="Ansh", age=20, city="Bangalore")

# Python collects the arguments like this:

# kwargs = {
#     "name": "Ansh",
#     "age": 20,
#     "city": "Bangalore"
# }

# Therefore:
#
# **kwargs → dictionary


# ============================================================
# 3. **KWARGS ONLY COLLECTS KEYWORD ARGUMENTS
# ============================================================

def show(**kwargs):
    print(kwargs)

show(name="Ansh", age=20)

# Valid


# This is NOT valid:

# show("Ansh", 20)

# Because "Ansh" and 20 are positional arguments,
# while **kwargs expects keyword arguments.


# ============================================================
# 4. ACCESSING VALUES
# ============================================================

def show(**kwargs):
    print(kwargs["name"])

show(name="Ansh", age=20)

# Output:
# Ansh


# We can access a value using its key:

# kwargs["name"]
# kwargs["age"]
# kwargs["city"]


# ============================================================
# 5. LOOPING THROUGH KEYS
# ============================================================

def show(**kwargs):

    for key in kwargs:
        print(key)

show(name="Ansh", age=20, city="Bangalore")

# Output:
# name
# age
# city


# By default, looping through a dictionary gives us
# its KEYS.


# ============================================================
# 6. LOOPING THROUGH KEY-VALUE PAIRS
# ============================================================

# To get both the key and value,
# use .items()

def show(**kwargs):

    for key, value in kwargs.items():
        print(key, value)

show(name="Ansh", age=20)

# Output:
# name Ansh
# age 20


# ============================================================
# 7. CUSTOM OUTPUT FORMAT
# ============================================================

def show(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)

show(name="Ansh", age=20, city="Bangalore")

# Output:
# name : Ansh
# age : 20
# city : Bangalore


# ============================================================
# 8. THE NAME "kwargs" IS NOT MANDATORY
# ============================================================

# The important part is **
#
# kwargs is just the standard naming convention.

def show(**data):
    print(data)

show(name="Ansh", age=20)

# Output:
# {'name': 'Ansh', 'age': 20}


# ============================================================
# 9. *ARGS VS **KWARGS
# ============================================================

# *args:
#
# Accepts variable number of POSITIONAL arguments.
#
# Stores them in a TUPLE.

def test(*args):
    print(args)

test(10, 20, 30)

# args = (10, 20, 30)


# **kwargs:
#
# Accepts variable number of KEYWORD arguments.
#
# Stores them in a DICTIONARY.

def test(**kwargs):
    print(kwargs)

test(a=10, b=20, c=30)

# kwargs = {
#     "a": 10,
#     "b": 20,
#     "c": 30
# }


# ============================================================
# 10. IMPORTANT COMPARISON
# ============================================================

# *args
#     ↓
# positional arguments
#     ↓
# tuple


# **kwargs
#     ↓
# keyword arguments
#     ↓
# dictionary


# ============================================================
# 11. NORMAL PARAMETER + **KWARGS
# ============================================================

def student(name, **kwargs):
    print(name)
    print(kwargs)

student("Ansh", age=20, city="Bangalore")

# Output:
# Ansh
# {'age': 20, 'city': 'Bangalore'}


# Here:
#
# "Ansh" → name
#
# age=20 and city="Bangalore"
# → collected inside kwargs


# ============================================================
# 12. *ARGS + **KWARGS
# ============================================================

def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(10, 20, name="Ansh", age=20)

# Output:
# (10, 20)
# {'name': 'Ansh', 'age': 20}


# Here:
#
# 10, 20
# → positional arguments
# → stored in args (tuple)
#
# name="Ansh", age=20
# → keyword arguments
# → stored in kwargs (dictionary)


# ============================================================
# 13. COMMON MISTAKE
# ============================================================

# This is WRONG:

# def test(**kwargs):
#     print(kwargs["name"])

# test(age=20)

# Why?
#
# Because "name" does not exist in kwargs.
#
# Accessing a missing dictionary key can cause:
# KeyError


# ============================================================
# QUICK MEMORY
# ============================================================

# *args:
# Variable number of positional arguments
# → tuple


# **kwargs:
# Variable number of keyword arguments
# → dictionary


# Most important syntax:

# def function(**kwargs):
#     ...


# Access a value:

# kwargs["key"]


# Loop through keys:

# for key in kwargs:
#     ...


# Loop through keys AND values:

# for key, value in kwargs.items():
#     ...


# ============================================================
# END OF **KWARGS NOTES
# ============================================================