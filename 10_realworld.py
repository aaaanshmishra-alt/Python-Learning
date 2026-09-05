#APPLE SHOP BILL GENERATOR CODE
price = int(input("Enter price of the apple: "))
quantity = int(input("Enter no of quantity of apple: "))

def apple(price , quantity):
    print("===== The Apple Shop =====")
    print("Price of a apple:",price)
    print("No of quantity:",quantity)
    print("Amount to be paid:",price * quantity)
    print("==== Thankyou visit again ====")

apple(price, quantity)