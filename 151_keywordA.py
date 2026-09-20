# ============================================================
# PRACTICE PROBLEM 1
# ============================================================

def employee(name, age, department):
    print(name, age, department)

# Call the function using keyword arguments.
# Your call should produce:
#
# Ansh 20 CSE
#
# But DON'T write the arguments in the order:
# name, age, department
# ============================================================
employee(age = 19, department = "Cse", name = "Suraj")