# ============================================================
# FINAL *ARGS CHECK
# ============================================================

def calculate(start, *numbers):
    total = start

    for number in numbers:
        total = total + number

    return total

print(calculate(10, 5, 15, 20))