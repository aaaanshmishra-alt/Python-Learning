#INTEREST RATE CALCULATOR
amount = int(input("Enter principal amount = "))
interest = int(input("Enter interest rate = "))
duration = int(input("Enter time period = "))

def loan(amount , interest , duration):
    print("===== Interest =====")
    print("Principal amount: ",amount)
    print("Interest rate: ",interest)
    print("The time period: ",duration)
    print("Simple interest: ", amount * interest * duration / 100)
    print("===================================")

loan(amount, interest , duration)