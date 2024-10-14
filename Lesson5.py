def triangular_number(n):
    return n * (n + 1) // 2

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get input from user
n = int(input("Give me a value of n: "))
print("Counting from j = 1 to %d:" %(n))

# Print the header
print("%5s %10s %15s" %('j', 'tri', 'fact'))

# Calculate and print triangular numbers and factorials
for j in range(1, n + 1):
    tri = triangular_number(j)
    fact = factorial(j)
    print("%5d %10d %15d" %(j, tri, fact))
