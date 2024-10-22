import math

def factorize(N):
    factors = []
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            factors.append(i)
            if i != N // i and i != 1:
                factors.append(N // i)
    return factors
    
print(factorize(6))
print(factorize(24))
print(factorize(0))
print(factorize(1))
print(factorize(7))


def sum_of_factors(factors):
    return sum(factors)



while True:
    try:
        N = int(input("Please input a number: "))
        if N < 1:
            print("Goodbye!")
            break
        factors = factorize(N)
        factor_sum = sum_of_factors(factors)
        print(f"Factor sum: {factor_sum}")

        if factor_sum == N:
            print(f"{N} is perfect")
        elif factor_sum > N:
            print(f"{N} is abundant")
        else:
            print(f"{N} is deficient")
    except ValueError:
        print("Please enter a valid positive integer.")

