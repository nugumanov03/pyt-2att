# Sum of Squares

import math
from itertools import combinations

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Step 1: Find primes of the form 4k+1
def primes_of_form_4k1(limit):
    primes = []
    for n in range(2, limit):
        if is_prime(n) and (n - 1) % 4 == 0:
            primes.append(n)
    return primes

# Step 2: Generate square-free numbers from the primes
def square_free_numbers(primes, max_value):
    square_free = set()
    for r in range(1, len(primes) + 1):
        for combo in combinations(primes, r):
            product = math.prod(combo)
            if product <= max_value:
                square_free.add(product)
    return sorted(square_free)

# Step 3: Find solutions to a^2 + b^2 = N
def solutions_for_n(n):
    solutions = []
    for a in range(int(math.sqrt(n)) + 1):
        b_squared = n - a**2
        if b_squared < 0:
            break
        b = int(math.sqrt(b_squared))
        if b**2 == b_squared and a <= b:
            solutions.append((a, b))
    return solutions

# Step 4: Compute S(N)
def S(n):
    solutions = solutions_for_n(n)
    return sum(a for a, b in solutions)

# Step 5: Main computation
def main():
    limit = 150
    primes = primes_of_form_4k1(limit)
    max_n = 10**6  # Adjust if needed
    square_free_ns = square_free_numbers(primes, max_n)
    result = sum(S(n) for n in square_free_ns)
    return result

# Run the main function
if __name__ == "__main__":
    print("Result:", main())
