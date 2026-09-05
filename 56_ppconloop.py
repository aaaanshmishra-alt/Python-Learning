#Print numbers from 1 to 30.
#Skip every number that is divisible by both 3 and 5 using continue.
i = 1
while i <= 30:
    if i % 3 == 0 and i % 5 == 0 :
        i = i + 1
        continue
    print(i)
    i = i + 1