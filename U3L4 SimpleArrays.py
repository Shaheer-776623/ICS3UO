ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
for i in range(len(ar2)):
  ar3 = ar2[i]
  for j in range(len(ar3)):
      print(ar3[j], end=" ")
  print() 

print(ar2) 

row_sums = []

for i in range(len(ar2)):
    row_sum = sum(ar2[i])  
    row_sums.append(row_sum)  
print("")
print(row_sums)

