# ============================================================
#                    PYTHON DICTIONARIES
# ============================================================


# ------------------------------------------------------------
# 1. WHAT IS A DICTIONARY?
# ------------------------------------------------------------
# A dictionary is a collection that stores data in
# KEY-VALUE pairs.
#
# Syntax:
# dictionary = {
#     key: value,
#     key: value
# }
#
# Example:

student = {
    "name": "Ansh",
    "age": 20,
    "branch": "CSE"
}

print(student)


# ------------------------------------------------------------
# 2. KEY AND VALUE
# ------------------------------------------------------------
# In a dictionary:
#
# key   → used to identify/access the data
# value → the actual data stored
#
# Example:

student = {
    "name": "Ansh",
    "age": 20,
    "branch": "CSE"
}

# Keys:
# "name"
# "age"
# "branch"
#
# Values:
# "Ansh"
# 20
# "CSE"


# ------------------------------------------------------------
# 3. ACCESSING VALUES USING KEYS
# ------------------------------------------------------------
# Dictionary values are accessed using their keys.
#
# Syntax:
# dictionary[key]

student = {
    "name": "Ansh",
    "age": 20,
    "branch": "CSE"
}

print(student["name"])
# Ansh

print(student["age"])
# 20

print(student["branch"])
# CSE


# ------------------------------------------------------------
# 4. DICTIONARY VS LIST
# ------------------------------------------------------------
# List:
#
# numbers = [10, 20, 30]
#
# Values are accessed using INDEX.

numbers = [10, 20, 30]

print(numbers[1])
# 20
#
#
# Dictionary:
#
# student = {"age": 20}
#
# Value is accessed using KEY.

student = {
    "age": 20
}

print(student["age"])
# 20
#
# Remember:
#
# List       → index → value
# Dictionary → key   → value


# ------------------------------------------------------------
# 5. ADDING A NEW KEY-VALUE PAIR
# ------------------------------------------------------------
# If the key does not already exist,
# assigning a value creates a new key-value pair.

student = {
    "name": "Ansh",
    "age": 20
}

student["branch"] = "CSE"

print(student)

# Output:
# {
#     "name": "Ansh",
#     "age": 20,
#     "branch": "CSE"
# }


# ------------------------------------------------------------
# 6. UPDATING A VALUE
# ------------------------------------------------------------
# If the key already exists, assigning a new value
# updates the existing value.

student = {
    "name": "Ansh",
    "age": 20
}

student["age"] = 22

print(student)

# Output:
# {
#     "name": "Ansh",
#     "age": 22
# }


# Remember:
#
# New key:
# dictionary["city"] = "Bangalore"
# → adds a new key-value pair
#
# Existing key:
# dictionary["age"] = 22
# → updates the value


# ------------------------------------------------------------
# 7. REMOVING A KEY-VALUE PAIR USING pop()
# ------------------------------------------------------------
# pop() removes a key and its corresponding value.
#
# Syntax:
# dictionary.pop(key)

student = {
    "name": "Ansh",
    "age": 20,
    "branch": "CSE"
}

student.pop("age")

print(student)

# Output:
# {
#     "name": "Ansh",
#     "branch": "CSE"
# }


# ------------------------------------------------------------
# 8. GETTING ALL KEYS USING keys()
# ------------------------------------------------------------
# keys() gives us all the keys in the dictionary.

student = {
    "name": "Ansh",
    "age": 20,
    "branch": "CSE"
}

print(student.keys())

# Conceptually:
# "name"
# "age"
# "branch"


# ------------------------------------------------------------
# 9. GETTING ALL VALUES USING values()
# ------------------------------------------------------------
# values() gives us all the values in the dictionary.

student = {
    "name": "Ansh",
    "age": 20,
    "branch": "CSE"
}

print(student.values())

# Conceptually:
# "Ansh"
# 20
# "CSE"


# ------------------------------------------------------------
# 10. GETTING KEY-VALUE PAIRS USING items()
# ------------------------------------------------------------
# items() gives us both the key and value together.

student = {
    "name": "Ansh",
    "age": 20,
    "branch": "CSE"
}

print(student.items())

# Conceptually:
# ("name", "Ansh")
# ("age", 20)
# ("branch", "CSE")


# ------------------------------------------------------------
# 11. LOOPING THROUGH DICTIONARY KEYS
# ------------------------------------------------------------
# When we directly loop through a dictionary,
# Python gives us the keys.

student = {
    "name": "Ansh",
    "age": 20
}

for key in student:
    print(key)

# Output:
# name
# age


# ------------------------------------------------------------
# 12. LOOPING THROUGH DICTIONARY VALUES
# ------------------------------------------------------------
# We can access values using:
#
# dictionary[key]

student = {
    "name": "Ansh",
    "age": 20
}

for key in student:
    print(student[key])

# Output:
# Ansh
# 20


# ------------------------------------------------------------
# 13. LOOPING THROUGH KEYS AND VALUES USING items()
# ------------------------------------------------------------
# items() allows us to get both the key and value
# during each iteration.

student = {
    "name": "Ansh",
    "age": 20,
    "branch": "CSE"
}

for key, value in student.items():
    print(key, value)

# Output:
# name Ansh
# age 20
# branch CSE


# ------------------------------------------------------------
# 14. PRINTING ONLY KEYS USING items()
# ------------------------------------------------------------
# Even though items() gives us both key and value,
# we can choose to print only the key.

student = {
    "name": "Ansh",
    "age": 20
}

for key, value in student.items():
    print(key)

# Output:
# name
# age


# ------------------------------------------------------------
# 15. PRINTING ONLY VALUES USING items()
# ------------------------------------------------------------
# We can also choose to print only the value.

student = {
    "name": "Ansh",
    "age": 20
}

for key, value in student.items():
    print(value)

# Output:
# Ansh
# 20


# ------------------------------------------------------------
# 16. CHECKING IF A KEY EXISTS
# ------------------------------------------------------------
# The 'in' operator checks whether a key exists
# in a dictionary.

student = {
    "name": "Ansh",
    "age": 20
}

print("name" in student)
# True

print("branch" in student)
# False


# ------------------------------------------------------------
# 17. CHECKING IF A VALUE EXISTS
# ------------------------------------------------------------
# By default, 'in' checks KEYS, not values.
#
# To check values, use values().

student = {
    "name": "Ansh",
    "age": 20
}

print("Ansh" in student)
# False
#
# "Ansh" is a value, not a key.

print("Ansh" in student.values())
# True


# ------------------------------------------------------------
# 18. DELETING USING del
# ------------------------------------------------------------
# del can be used to remove a specific key-value pair.

student = {
    "name": "Ansh",
    "age": 20,
    "branch": "CSE"
}

del student["age"]

print(student)

# Output:
# {
#     "name": "Ansh",
#     "branch": "CSE"
# }


# ------------------------------------------------------------
# 19. DELETING THE ENTIRE DICTIONARY
# ------------------------------------------------------------
# del can also delete the entire dictionary.

student = {
    "name": "Ansh",
    "age": 20
}

del student

# The dictionary variable no longer exists.


# ------------------------------------------------------------
# 20. DICTIONARY WITH DIFFERENT DATA TYPES
# ------------------------------------------------------------
# Dictionary values can contain different data types.

student = {
    "name": "Ansh",
    "age": 20,
    "percentage": 85.5,
    "passed": True
}

print(student)


# ------------------------------------------------------------
# 21. DICTIONARY VALUES CAN BE LISTS
# ------------------------------------------------------------
# A dictionary value can also be a List.

student = {
    "name": "Ansh",
    "subjects": ["Python", "Java", "DSA"]
}

print(student["subjects"])

# Output:
# ["Python", "Java", "DSA"]


# We can access an element from that List:

print(student["subjects"][0])
# Python


# ------------------------------------------------------------
# 22. DICTIONARY VALUES CAN BE TUPLES
# ------------------------------------------------------------
# A dictionary value can also be a Tuple.

student = {
    "name": "Ansh",
    "marks": (80, 85, 90)
}

print(student["marks"])

# Output:
# (80, 85, 90)


# ------------------------------------------------------------
# 23. NESTED DICTIONARIES
# ------------------------------------------------------------
# A dictionary can contain another dictionary
# as a value.

students = {
    "student1": {
        "name": "Ansh",
        "age": 20
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}

print(students["student1"]["name"])
# Ansh

print(students["student2"]["age"])
# 21


# ============================================================
#                    IMPORTANT SUMMARY
# ============================================================

# student = {
#     "name": "Ansh",
#     "age": 20
# }
# → creates a dictionary


# student["name"]
# → accesses a value using its key


# student["city"] = "Bangalore"
# → adds a new key-value pair


# student["age"] = 21
# → updates an existing value


# student.pop("age")
# → removes a key-value pair


# student.keys()
# → returns all keys


# student.values()
# → returns all values


# student.items()
# → returns key-value pairs


# "age" in student
# → checks whether "age" is a key


# "Ansh" in student.values()
# → checks whether "Ansh" is a value


# del student["age"]
# → deletes a specific key-value pair


# del student
# → deletes the entire dictionary


# for key in student:
#     print(key)
# → loops through keys


# for key in student:
#     print(student[key])
# → loops through values


# for key, value in student.items():
#     print(key, value)
# → loops through keys and values


# ============================================================
#               MOST IMPORTANT DIFFERENCE
# ============================================================

# LIST:
# numbers = [10, 20, 30]
# numbers[0]
# → access using INDEX


# TUPLE:
# numbers = (10, 20, 30)
# numbers[0]
# → access using INDEX


# DICTIONARY:
# numbers = {
#     "first": 10,
#     "second": 20
# }
#
# numbers["first"]
# → access using KEY


# Remember:
#
# LIST       → index → value
# TUPLE      → index → value
# DICTIONARY → key   → value
#
# Dictionary's biggest idea:
# KEY → VALUE