import math

print("%3s|%5s|%7s|%5s" %("N","SQR","Cubes","Roots"))
print("|--+-----+-------+-----|")

for x in range(10, 201, 15):
  N = x
  N2 = x**2
  N3 = x**3
  Nsqrt = math.sqrt(N)
  
  
  print("%3d|%5d|%7d|%5.2f" %(N,N2,N3,Nsqrt))
  
