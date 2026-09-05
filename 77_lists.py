# ============================================================
#                         PYTHON LISTS
# ============================================================


# ------------------------------------------------------------
# 1. CREATING A LIST
# ------------------------------------------------------------
# A list stores multiple values inside a single variable.
# Lists are created using square brackets [].

numbers = [10, 20, 30, 40]


# ------------------------------------------------------------
# 2. LIST CAN STORE DIFFERENT DATA TYPES
# ------------------------------------------------------------
# A list can contain different types of values.

student = ["Ansh", 19, 8.5, True]


# ------------------------------------------------------------
# 3. INDEXING
# ------------------------------------------------------------
# Every element in a list has an index.
# Python indexing starts from 0.

numbers = [10, 20, 30, 40]

print(numbers[0])   # 10
print(numbers[1])   # 20
print(numbers[2])   # 30
print(numbers[3])   # 40


# ------------------------------------------------------------
# 4. NEGATIVE INDEXING
# ------------------------------------------------------------
# Negative indexes allow us to access elements from the end.
#
# -1 = last element
# -2 = second-last element
# -3 = third-last element

numbers = [10, 20, 30, 40]

print(numbers[-1])  # 40
print(numbers[-2])  # 30


# ------------------------------------------------------------
# 5. CHANGING / MODIFYING AN ELEMENT
# ------------------------------------------------------------
# We can change an element using its index.
#
# Syntax:
# list[index] = new_value

numbers = [10, 20, 30, 40]

numbers[2] = 99

print(numbers)
# [10, 20, 99, 40]


# ------------------------------------------------------------
# 6. append()
# ------------------------------------------------------------
# append() adds ONE element at the end of the list.

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
# [10, 20, 30, 40]


# ------------------------------------------------------------
# 7. insert()
# ------------------------------------------------------------
# insert() adds an element at a specific index.
#
# Syntax:
# list.insert(index, value)

numbers = [10, 20, 30, 40]

numbers.insert(2, 25)

print(numbers)
# [10, 20, 25, 30, 40]


# ------------------------------------------------------------
# 8. remove()
# ------------------------------------------------------------
# remove() removes the FIRST occurrence of a VALUE.

numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
# [10, 30, 20]


# ------------------------------------------------------------
# 9. pop(index)
# ------------------------------------------------------------
# pop() removes an element using its INDEX.

numbers = [10, 20, 30, 40]

numbers.pop(2)

print(numbers)
# [10, 20, 40]


# ------------------------------------------------------------
# 10. pop() WITHOUT AN INDEX
# ------------------------------------------------------------
# If no index is given, pop() removes the LAST element.

numbers = [10, 20, 30, 40]

numbers.pop()

print(numbers)
# [10, 20, 30]


# ------------------------------------------------------------
# 11. del
# ------------------------------------------------------------
# del can remove an element using its index.

numbers = [10, 20, 30, 40]

del numbers[2]

print(numbers)
# [10, 20, 40]


# ------------------------------------------------------------
# 12. len()
# ------------------------------------------------------------
# len() tells us the NUMBER OF ELEMENTS in a list.

numbers = [10, 20, 30, 40]

print(len(numbers))
# 4
#
# Number of elements = 4
# Last index = 3
#
# Last index = len(list) - 1


# ------------------------------------------------------------
# 13. in
# ------------------------------------------------------------
# 'in' checks whether a value exists in a list.
# It returns True or False.

numbers = [10, 20, 30, 40]

print(20 in numbers)
# True

print(25 in numbers)
# False


# ------------------------------------------------------------
# 14. not in
# ------------------------------------------------------------
# 'not in' checks whether a value DOES NOT exist in a list.

numbers = [10, 20, 30, 40]

print(25 not in numbers)
# True


# ------------------------------------------------------------
# 15. BASIC SLICING
# ------------------------------------------------------------
# Slicing is used to get multiple elements from a list.
#
# Syntax:
# list[start:stop]
#
# start = included
# stop = NOT included

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
# [20, 30, 40]


# ------------------------------------------------------------
# 16. SLICING FROM THE BEGINNING
# ------------------------------------------------------------
# If start is omitted, slicing starts from index 0.

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
# [10, 20, 30]


# ------------------------------------------------------------
# 17. SLICING UNTIL THE END
# ------------------------------------------------------------
# If stop is omitted, slicing continues until the end.

numbers = [10, 20, 30, 40, 50]

print(numbers[2:])
# [30, 40, 50]


# ------------------------------------------------------------
# 18. SLICING WITH STEP
# ------------------------------------------------------------
# Syntax:
# list[start:stop:step]
#
# step tells Python how many positions to move.

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:6:2])
# [10, 30, 50]


# Another example:

print(numbers[1:6:2])
# [20, 40, 60]


# ------------------------------------------------------------
# 19. LOOPING THROUGH A LIST
# ------------------------------------------------------------
# We can directly loop through the values of a list.

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)

# Output:
# 10
# 20
# 30
# 40


# ------------------------------------------------------------
# 20. LOOPING THROUGH INDEXES
# ------------------------------------------------------------
# We can use range() and len() to loop through indexes.

numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(i)

# Output:
# 0
# 1
# 2


# ------------------------------------------------------------
# 21. ACCESSING VALUES USING INDEXES IN A LOOP
# ------------------------------------------------------------
# Here i represents the index.
# numbers[i] gives the value at that index.

numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(numbers[i])

# Output:
# 10
# 20
# 30


# ------------------------------------------------------------
# 22. sort()
# ------------------------------------------------------------
# sort() arranges the list in ASCENDING order.
# It changes the original list.

numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
# [10, 20, 30, 40]


# ------------------------------------------------------------
# 23. sort(reverse=True)
# ------------------------------------------------------------
# sort(reverse=True) arranges the list in DESCENDING order.

numbers = [10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)
# [40, 30, 20, 10]


# ------------------------------------------------------------
# 24. reverse()
# ------------------------------------------------------------
# reverse() reverses the CURRENT order of the list.
# It does NOT sort the list.

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
# [40, 30, 20, 10]


# ------------------------------------------------------------
# 25. sort() + reverse()
# ------------------------------------------------------------
# We can first sort and then reverse.
# This gives descending order.

numbers = [5, 2, 8, 1]

numbers.sort()
# [1, 2, 5, 8]

numbers.reverse()
# [8, 5, 2, 1]

print(numbers)


# ------------------------------------------------------------
# 26. extend()
# ------------------------------------------------------------
# extend() adds MULTIPLE elements from another iterable/list.

numbers = [1, 2]

numbers.extend([3, 4, 5])

print(numbers)
# [1, 2, 3, 4, 5]


# ------------------------------------------------------------
# 27. append() vs extend()
# ------------------------------------------------------------
# append() adds the entire object as ONE element.

numbers = [1, 2]

numbers.append([3, 4, 5])

print(numbers)
# [1, 2, [3, 4, 5]]


# extend() adds the elements individually.

numbers = [1, 2]

numbers.extend([3, 4, 5])

print(numbers)
# [1, 2, 3, 4, 5]


# ------------------------------------------------------------
# 28. COPYING A LIST
# ------------------------------------------------------------
# If we do:
#
# new_numbers = numbers
#
# both variables refer to the SAME list.
# It does NOT create an independent copy.

numbers = [1, 2, 3]

new_numbers = numbers

new_numbers.append(4)

print(numbers)
# [1, 2, 3, 4]


# ------------------------------------------------------------
# 29. copy()
# ------------------------------------------------------------
# copy() creates a separate list.

numbers = [1, 2, 3]

new_numbers = numbers.copy()

new_numbers.append(4)

print(numbers)
# [1, 2, 3]

print(new_numbers)
# [1, 2, 3, 4]


# ------------------------------------------------------------
# 30. NESTED LISTS
# ------------------------------------------------------------
# A nested list is a list containing other lists.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# ------------------------------------------------------------
# 31. ACCESSING AN INNER LIST
# ------------------------------------------------------------
# matrix[0] gives the first inner list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
# [1, 2, 3]


# ------------------------------------------------------------
# 32. ACCESSING AN ELEMENT INSIDE A NESTED LIST
# ------------------------------------------------------------
# Syntax:
# matrix[row][column]
#
# First index = selects the inner list
# Second index = selects the element inside that list.

matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(matrix[1][0])
# 30

print(matrix[2][1])
# 60


# ------------------------------------------------------------
# 33. MODIFYING A NESTED LIST
# ------------------------------------------------------------
# We can change an element inside a nested list.

matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]

matrix[1][0] = 99

print(matrix)

# [
#     [10, 20],
#     [99, 40],
#     [50, 60]
# ]


# ============================================================
#                    IMPORTANT SUMMARY
# ============================================================

# list[index]
#       → access an element

# list[index] = value
#       → change an element

# list.append(value)
#       → add ONE element at the end

# list.insert(index, value)
#       → add an element at a specific position

# list.remove(value)
#       → remove the first occurrence of a VALUE

# list.pop(index)
#       → remove an element using its INDEX

# list.pop()
#       → remove the LAST element

# del list[index]
#       → delete an element using its INDEX

# len(list)
#       → number of elements

# value in list
#       → check whether value exists

# value not in list
#       → check whether value does not exist

# list[start:stop]
#       → slicing

# list[start:stop:step]
#       → slicing with step

# list.sort()
#       → ascending order

# list.sort(reverse=True)
#       → descending order

# list.reverse()
#       → reverse current order

# list.extend(other_list)
#       → add multiple elements

# list.copy()
#       → create an independent copy

# list[row][column]
#       → access an element in a nested list