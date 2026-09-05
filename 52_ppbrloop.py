#Print numbers from 1 to 20.
#The moment you encounter the first multiple of 9, stop the loop using break.
i = 1
while i <= 20:
    if i % 9 == 0:
        break
    print(i)
    i = i + 1