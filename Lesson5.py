import math

n = int(input("Please input a value for n: "))

print ("Counting form j = 1 to %d:\n" %n)

print("j    tri    factorial")
print("--------------------------")
for i in range (1, n + 1):
  print("%d    %d        %d" %(i, i**2, math.factorial(i)))
