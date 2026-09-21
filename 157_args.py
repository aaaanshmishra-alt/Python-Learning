# ============================================================
# PRACTICE PROBLEM 2 — *ARGS
# ============================================================

# Create a function called count_numbers()
#
# It should accept ANY number of positional arguments
# and return how many arguments were passed.
#
# Example:
#
# count_numbers(10, 20, 30)
# → 3
#
# count_numbers(5, 10, 15, 20, 25)
# → 5
#
# Use *args.
# ============================================================

def count_numbers(*args):
    return len(args)
print(count_numbers(10, 20, 30))


