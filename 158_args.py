# ============================================================
# PRACTICE PROBLEM 3 — *ARGS
# ============================================================

# Create a function called find_max()
#
# It should accept ANY number of positional arguments
# and return the largest number.
#
# Example:
#
# find_max(10, 25, 7, 40, 15)
# → 40
#
# find_max(5, 100, 20)
# → 100
#
# Use *args.
# ============================================================
def find_max(*args):
    highest = args[0]
    for number in args:
        if number > highest:
            highest = number
    return highest
print(find_max(10, 25, 7, 40, 15))