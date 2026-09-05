#The secret number is:7 
#Write a program that keeps asking the user to guess the secret number.
#If the user guesses the wrong number, print: Wrong ! Try again
#If the user guesses 7, print: correct guess

while True:
    Guess = int(input("Guess the number: "))
    if Guess == 7:
        break
    print("Wrong guess! Try again")
print("correct guess")