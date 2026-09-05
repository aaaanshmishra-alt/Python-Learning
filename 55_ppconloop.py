#Print numbers from 1 to 20, but skip all even numbers using continue.
i = 1 
while i <= 20:
    if i % 2 == 0:
        i = i + 1
        continue
    print(i)
    i = i + 1
