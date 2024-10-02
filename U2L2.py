import math

x = input("Please input a whole number: ")
x = int(x)

if (x >= 1) and (x<=20):
  y = input("Please input another nonzero whole number")
y = int(y)
rem = 1
if (y != 0):
  rem = x % y
  print("Now deciding if", y, "is a factor of", x, "...")
else:
  print ("You can't input a zero!")

if rem == 0:
    print("Yes!", y, "is a factor of", x) 
