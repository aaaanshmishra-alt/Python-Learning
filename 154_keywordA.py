# ============================================================
# FINAL PRACTICE — KEYWORD ARGUMENTS
# ============================================================

def product(name, price, quantity=1, discount=0):
    total = price * quantity
    total = total - discount
    print(name, total)

# Call the function so that the output is:
#
# Laptop 45000
#
# Use at least TWO keyword arguments.
#
# Write only the function call.
# ============================================================
product("Laptop", price = 90000, discount = 45000, quantity = 1)