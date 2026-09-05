# ============================================================
#                         PYTHON SETS
# ============================================================


# ------------------------------------------------------------
# 1. WHAT IS A SET?
# ------------------------------------------------------------
# A Set is a collection used to store UNIQUE values.
#
# The most important property of a Set:
# → Duplicate elements are automatically removed.
#
# Sets are unordered collections.

numbers = {10, 20, 30, 20, 10}

print(numbers)

# Conceptually:
# {10, 20, 30}
#
# Do NOT rely on the order in which a Set is displayed.


# ------------------------------------------------------------
# 2. CREATING A SET
# ------------------------------------------------------------
# Sets are generally created using curly braces {}.

numbers = {10, 20, 30}

print(numbers)


# Compare:
#
# List  → [10, 20, 30]
# Tuple → (10, 20, 30)
# Set   → {10, 20, 30}


# ------------------------------------------------------------
# 3. EMPTY SET
# ------------------------------------------------------------
# IMPORTANT:
#
# {} creates an EMPTY DICTIONARY, NOT an empty Set.

empty = {}

print(type(empty))
# dict


# To create an empty Set:

empty = set()

print(type(empty))
# set


# Remember:
#
# {}      → empty dictionary
# set()   → empty Set


# ------------------------------------------------------------
# 4. SETS AUTOMATICALLY REMOVE DUPLICATES
# ------------------------------------------------------------
# Duplicate values are stored only once.

numbers = {10, 20, 10, 30, 20, 10}

print(numbers)

# Conceptually:
# {10, 20, 30}


# ------------------------------------------------------------
# 5. CONVERTING A LIST INTO A SET
# ------------------------------------------------------------
# Converting a List into a Set is a common way to
# remove duplicate values.

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)

# Conceptually:
# {10, 20, 30, 40}


# ------------------------------------------------------------
# 6. SETS DO NOT HAVE INDEXES
# ------------------------------------------------------------
# Lists and Tuples support indexing.

numbers = [10, 20, 30]
print(numbers[0])
# 10

numbers = (10, 20, 30)
print(numbers[0])
# 10


# Sets do NOT support indexing.

numbers = {10, 20, 30}

# print(numbers[0])
# ❌ TypeError


# Remember:
#
# List  → indexed
# Tuple → indexed
# Set   → NOT indexed


# ------------------------------------------------------------
# 7. ADDING ONE ELEMENT USING add()
# ------------------------------------------------------------
# add() adds one element to a Set.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

# Conceptually:
# {10, 20, 30, 40}


# If the element already exists, nothing new is added.

numbers.add(20)

# 20 is already present.
# The Set still contains only one 20.


# ------------------------------------------------------------
# 8. REMOVING AN ELEMENT USING remove()
# ------------------------------------------------------------
# remove() removes a specific element.

numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)

# Conceptually:
# {10, 30, 40}


# IMPORTANT:
# If the element does not exist, remove() gives an error.

# numbers.remove(50)
# ❌ Error


# ------------------------------------------------------------
# 9. REMOVING AN ELEMENT USING discard()
# ------------------------------------------------------------
# discard() also removes an element.

numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)

# Conceptually:
# {10, 30}


# IMPORTANT:
# If the element does not exist, discard() does NOT
# give an error.

numbers.discard(50)

# No error.
# Nothing happens.


# Remember:
#
# remove(value)
# → removes value
# → error if value doesn't exist
#
# discard(value)
# → removes value
# → no error if value doesn't exist


# ------------------------------------------------------------
# 10. CHECKING IF AN ELEMENT EXISTS
# ------------------------------------------------------------
# The 'in' operator checks membership in a Set.

numbers = {10, 20, 30}

print(20 in numbers)
# True

print(50 in numbers)
# False


# 'not in' can also be used.

print(50 not in numbers)
# True


# ------------------------------------------------------------
# 11. LENGTH OF A SET
# ------------------------------------------------------------
# len() returns the number of UNIQUE elements.

numbers = {10, 20, 30, 40}

print(len(numbers))
# 4


numbers = {10, 20, 20, 30, 30}

print(len(numbers))
# 3
#
# Because the Set contains:
# {10, 20, 30}


# ------------------------------------------------------------
# 12. LOOPING THROUGH A SET
# ------------------------------------------------------------
# We can use a for loop to visit Set elements.

numbers = {10, 20, 30}

for number in numbers:
    print(number)

# The loop visits all elements.
#
# IMPORTANT:
# Do NOT rely on the order of elements in a Set.


# ------------------------------------------------------------
# 13. CLEARING A SET USING clear()
# ------------------------------------------------------------
# clear() removes all elements from the Set.

numbers = {10, 20, 30, 40}

numbers.clear()

print(numbers)

# Output:
# set()


# The Set still exists, but it is empty.


# ------------------------------------------------------------
# 14. DELETING A SET USING del
# ------------------------------------------------------------
# del deletes the entire Set variable.

numbers = {10, 20, 30}

del numbers

# The variable 'numbers' no longer exists.


# Difference:
#
# clear()
# → removes all elements
# → Set still exists
#
# del
# → deletes the entire variable


# ------------------------------------------------------------
# 15. ADDING MULTIPLE ELEMENTS USING update()
# ------------------------------------------------------------
# add() adds ONE element.
# update() can add MULTIPLE elements.

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)

# Conceptually:
# {10, 20, 30, 40, 50, 60}


# update() can also accept other collections.

numbers.update((70, 80))


# ------------------------------------------------------------
# 16. SET pop()
# ------------------------------------------------------------
# pop() removes and returns an ARBITRARY element from a Set.

numbers = {10, 20, 30, 40}

removed = numbers.pop()

print(removed)
print(numbers)

# IMPORTANT:
# You should NOT assume which element will be removed.


# Difference:
#
# List.pop()
# → removes the last element by default
#
# Set.pop()
# → removes an arbitrary element


# ------------------------------------------------------------
# 17. SET UNION
# ------------------------------------------------------------
# Union combines ALL unique elements from both Sets.

A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))

# Conceptually:
# {1, 2, 3, 4, 5}


# Union can also be performed using:

print(A | B)

# | means UNION


# ------------------------------------------------------------
# 18. SET INTERSECTION
# ------------------------------------------------------------
# Intersection gives elements that are COMMON
# to both Sets.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.intersection(B))

# Output:
# {3, 4}


# Intersection can also be written as:

print(A & B)

# & means INTERSECTION


# ------------------------------------------------------------
# 19. SET DIFFERENCE
# ------------------------------------------------------------
# Difference gives elements that are in the FIRST Set
# but NOT in the second Set.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.difference(B))

# Output:
# {1, 2}


# Difference can also be written as:

print(A - B)

# - means DIFFERENCE


# IMPORTANT:
# Direction matters.

print(B.difference(A))
# {5, 6}

# A - B is NOT necessarily equal to B - A.


# ------------------------------------------------------------
# 20. SYMMETRIC DIFFERENCE
# ------------------------------------------------------------
# Symmetric difference gives elements that are in
# EITHER Set but NOT in BOTH.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.symmetric_difference(B))

# Output:
# {1, 2, 5, 6}


# Symmetric difference can also be written as:

print(A ^ B)

# ^ means SYMMETRIC DIFFERENCE


# ------------------------------------------------------------
# 21. SUBSET — issubset()
# ------------------------------------------------------------
# issubset() checks whether ALL elements of one Set
# are present in another Set.

A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))

# Output:
# True


# It can also be written as:

print(A <= B)

# <= means subset


# ------------------------------------------------------------
# 22. SUPERSET — issuperset()
# ------------------------------------------------------------
# issuperset() checks whether one Set contains
# ALL elements of another Set.

A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))

# Output:
# True


# It can also be written as:

print(A >= B)

# >= means superset


# ------------------------------------------------------------
# 23. DISJOINT SETS — isdisjoint()
# ------------------------------------------------------------
# isdisjoint() checks whether two Sets have
# NO elements in common.

A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))

# Output:
# True


# If they have at least one common element:

A = {1, 2, 3}
B = {3, 4, 5}

print(A.isdisjoint(B))

# Output:
# False


# ============================================================
#                  SET OPERATIONS SUMMARY
# ============================================================

# A = {1, 2, 3}
# B = {3, 4, 5}


# A.union(B)
# → {1, 2, 3, 4, 5}
# → everything from both


# A.intersection(B)
# → {3}
# → common elements


# A.difference(B)
# → {1, 2}
# → elements in A but NOT B


# B.difference(A)
# → {4, 5}
# → elements in B but NOT A


# A.symmetric_difference(B)
# → {1, 2, 4, 5}
# → elements in either Set, but NOT both


# ============================================================
#                 SET OPERATORS SUMMARY
# ============================================================

# A | B
# → Union


# A & B
# → Intersection


# A - B
# → Difference


# A ^ B
# → Symmetric Difference


# A <= B
# → A is a subset of B


# A >= B
# → A is a superset of B


# ============================================================
#                  IMPORTANT SET METHODS
# ============================================================

# add(value)
# → add one element


# update(collection)
# → add multiple elements


# remove(value)
# → remove element
# → error if element doesn't exist


# discard(value)
# → remove element
# → no error if element doesn't exist


# pop()
# → remove an arbitrary element


# clear()
# → remove all elements


# union()
# → combine Sets


# intersection()
# → common elements


# difference()
# → elements only in first Set


# symmetric_difference()
# → elements in either Set but not both


# issubset()
# → check if Set is contained inside another Set


# issuperset()
# → check if Set contains another Set


# isdisjoint()
# → check if Sets have no common elements


# ============================================================
#                    MOST IMPORTANT
# ============================================================

# LIST:
# numbers = [10, 20, 30]
# → ordered
# → indexed
# → allows duplicates
# → mutable


# TUPLE:
# numbers = (10, 20, 30)
# → ordered
# → indexed
# → allows duplicates
# → immutable


# SET:
# numbers = {10, 20, 30}
# → unordered
# → NOT indexed
# → does NOT allow duplicates
# → useful for membership and mathematical set operations


# Remember:
#
# LIST  → ordered + mutable + duplicates allowed
#
# TUPLE → ordered + immutable + duplicates allowed
#
# SET   → unordered + unique values + no indexing

#Union                 → EVERYTHING
#Intersection          → COMMON
#Difference            → ONLY IN FIRST
#Symmetric Difference  → EVERYTHING EXCEPT COMMON