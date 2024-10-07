# Initialize an empty list to store the items
items = []

# Prompt the user to enter the number of items
num_items = int(input("Enter the number of items: "))

# Loop to get each item from the user
for i in range(num_items):
    item = input("Enter item {}: ".format(i+1))
    items.append(item)



# Print the number of items
print("The number of items is %d." % len(items))

# Print each item in the list (Prediction C)
for i in items:
    print(i)

