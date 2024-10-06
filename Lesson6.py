print("--8<--" * 10)
print ("")
S = "#"
for i in range (11, 0, -1):
  print(S * i)
  
space = " "
s = 5
for hA in range(1,12,2):
  print("%s%s" %(space * s, S * hA))
  s -= 1
print ("")

space = " "
s = 5
for hA in range(1,12,2):
  print("%s%s" %(space * s, S * hA))
  s -= 1
  
s += 1
for hB in range(9, 0, -2):
  s += 1
  print("%s%s" %(space * s, S * hB))
