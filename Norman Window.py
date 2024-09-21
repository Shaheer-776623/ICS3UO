import math
length = input("Please input a length: ")
length = float(length)
area1 = math.pow(length, 2)

(print)("\nThe area of the square part of the norman window with a side length of", length, "is:", area1, )
radius = length / 2
radius = float(radius)
π = math.pi
formula_radius = math.pow(radius, 2)

area2 = (0.5*π*formula_radius) 
print("\nThe area of the semi-circle part of the norman window is: ", area1)

area3 = area2 + area1
print("\nThe area of the Norman Window of side length ", length, "is: ", area3)
