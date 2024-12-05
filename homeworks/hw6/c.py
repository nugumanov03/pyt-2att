# n-sequences

def f(n, mod=1_000_000_009):
    # Initialize a list to store the contributions for each sequence length
    dp = [0] * (n + 1)
    dp[1] = n  # Base case: L(S) = 1 for all sequences of length 1
    
    # Compute contributions for sequences of increasing lengths
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] * n + i * pow(n, i, mod)) % mod
    
    # Sum all contributions to get f(n)
    return dp[n]

# Calculate f(7,500,000) mod 1,000,000,009
result = f(7_500_000)
print(result)
