# ============================================================
# PRACTICE PROBLEM 3
# ============================================================

def introduce(name, age=18, city="Bangalore"):
    print(name, age, city)

# Call the function to produce:
#
# Ansh 20 Mumbai
#
# Requirements:
# 1. name must be positional.
# 2. age and city must be keyword arguments.
# 3. Do NOT use the default values for age and city.
# ============================================================
introduce("Ansh", age = 20, city = "Mumbai")