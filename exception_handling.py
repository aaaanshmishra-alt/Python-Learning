salary = 10000

daysInMonth = input("Days in the month: ")
daysAttended = input("Days attended in month: ")

try:
    daysInMonth = int(daysInMonth)
    daysAttended = int(daysAttended)

    pay = round(salary * daysAttended / daysInMonth)
    print("Your pay is:", pay)

except ZeroDivisionError as e:
    print("Zero Division Error has occurred")
    print(e)

except ValueError as e:
    print("Value Error")
    print(e)

except Exception as e:
    print("Exception:", e)