# Guessing Game

import math

# Compute Fibonacci numbers up to F30
def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

# Recursive cost function for small n
def compute_C(n, a, b):
    if n == 1:
        return 0
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = float('inf')
        for x in range(1, i + 1):
            cost = max(a + dp[x - 1], b + dp[i - x])
            dp[i] = min(dp[i], cost)
    return dp[n]

# Approximate C(n, a, b) for large n
def large_C(n, a, b):
    log_ratio = math.log(b / a)
    return math.log(n) / (log_ratio if log_ratio != 0 else 1)

# Main calculation
def sum_C(n, max_k):
    fib = fibonacci(max_k)
    total_sum = 0
    for k in range(1, max_k + 1):
        a = k
        b = fib[k - 1]
        if n <= 1000:
            total_sum += compute_C(n, a, b)
        else:
            total_sum += large_C(n, a, b)
    return total_sum

# Compute the result for n = 10^12 and k = 1 to 30
n = 10**12
max_k = 30
result = sum_C(n, max_k)
print(f"{result:.8f}")
