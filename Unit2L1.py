print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
elif (ch== "C"):
    print("I prefer cherries")
else:
    print("That is not an option on the menu!")
  

print("\n\n\nPart B: Marking system")

mark = input("\nWhat is your mark?: ")
mark = float(mark)

if (mark <= 100) and (mark >= 80):
  print("Your mark is an A!")
elif (mark <= 79) and (mark >= 70):
  print("Your mark is a B!")
elif (mark <= 69) and (mark >= 60):
  print("Your mark is a C!")
elif (mark <= 59) and (mark >=50):
  print("Your mark is a D")
elif (mark < 50):
  print("Your mark is an F")
else:
  print("Invalid number")











