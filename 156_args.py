# ============================================================
# PRACTICE PROBLEM 1 — *ARGS
# ============================================================

# Create a function called total_sum()
#
# It should accept ANY number of positional arguments
# and return their total.
#
# Example:
#
# total_sum(10, 20, 30)
# → 60
#
# total_sum(5, 10, 15, 20, 25)
# → 75
#
# Use *args.
# ============================================================

def total_sum(*args):
    total = 0
    for numbers in args:
        total = total + numbers
    return total
print(total_sum(10, 20, 30))

 