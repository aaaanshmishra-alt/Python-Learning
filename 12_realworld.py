#REPORT CARD OF THE STUDENT
name = input("Enter your name: ")
m1 = int(input("Marks in english: "))
m2 = int(input("Marks in Maths: "))
m3 = int(input("Marks in Science: "))

def marks(name, m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3

    print("===== REPORT CARD =====")
    print("Name:", name)
    print("English:", m1)
    print("Maths:", m2)
    print("Science:", m3)
    print("Total:", total)
    print("Average:", average)
    print("====================")

marks(name, m1, m2, m3)

 
 