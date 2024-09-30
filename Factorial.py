total = 1
n = int(input("Enter a whole number more than 0: "))
count = 0

print("Factorial number 0 is 1")
  
while (count <= n):
  count = count + 1
  total = total * count
  print ("Factorial number", count, "is", total)
