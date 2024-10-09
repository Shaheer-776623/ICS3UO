import math

n = int(input("Please input a value for n: "))

print ("Counting from j = 1 to %d:\n" %n)

print("j    tri    factorial")
print("--------------------------")

total = 1
count = 1

total2 = 1
count2 = 0

  
for n in range (1, n + 1):
  while (count < n) and (count2 <= n):
    count = count + 1
    total = total + count
    count2 = count2 + 1
    total2 = total2 * count2
    print("%d %5d %10d" %(n - 1 , total, total2))
