#Print numbers from 1 to 25.
#Skip every number that is:
#* divisible by 2
#* or divisible by 5
#using continue.

i = 1
while i <= 25:
    if i % 2 == 0 or i % 5 == 0:
        i = i +1
        continue
    print(i)
    i = i + 1