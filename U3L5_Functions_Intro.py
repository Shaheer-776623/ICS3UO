import math

def add(a, b):
    return a + b

try:
    a = float(input("Enter the first number (for a): "))
    b = float(input("Enter the second number (for b): "))
    result = add(a, b) * 2
    print("Result of add(a, b) * 2: ", result)
except ValueError:
    print("Please enter valid numerical values.")

def myPow(m, n):
    return m ** n

try:
    pow_result = myPow(a, b)
    math_pow_result = math.pow(a, b)
    print("Result of myPow(a, b): ", pow_result)
    print("Result of math.pow(a, b): ", math_pow_result)
except ValueError:
    print("Please enter valid numerical values.")
    

