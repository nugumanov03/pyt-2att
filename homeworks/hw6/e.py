# 10-substrings

MOD = 1000000007

def count_10_friendly(num):
    num_str = str(num)
    n = len(num_str)

    # Memoization for DP states
    dp = {}

    # Recursive function with memoization
    def dfs(pos, sum, tight, valid):
        # Base case: Reached the end
        if pos == n:
            return 1 if valid else 0

        # Memoization key
        state = (pos, sum, tight, valid)
        if state in dp:
            return dp[state]

        # Limits for the current digit (0 to 9 if not tight, else 0 to digit[pos])
        limit = int(num_str[pos]) if tight else 9

        # Total count of valid numbers
        count = 0
        for digit in range(0, limit + 1):
            # Update the sum and validity based on the current digit
            new_sum = (sum + digit) % 10
            new_valid = valid or (new_sum == 0 and sum != 0)
            count += dfs(pos + 1, new_sum, tight and (digit == limit), new_valid)
            count %= MOD

        dp[state] = count
        return count

    # Start DFS with the initial state
    return dfs(0, 0, True, False)


# Compute T(10^18)
def compute_T(n):
    return count_10_friendly(n)

# Run the computation for T(10^18)
n = 10**18
result = compute_T(n) % MOD
print(result)
