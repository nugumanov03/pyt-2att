# Jumping frog

MOD = 10**9

# Compute f(n) modulo 10^9
def compute_f(n):
    f = [0] * (n + 1)
    f[1], f[2], f[3] = 1, 1, 2
    for i in range(4, n + 1):
        f[i] = (f[i - 1] + f[i - 2] + f[i - 3]) % MOD
    return f

# Modular exponentiation for x^y % MOD
def mod_exp(x, y, mod):
    res = 1
    while y:
        if y % 2 == 1:
            res = (res * x) % mod
        x = (x * x) % mod
        y //= 2
    return res

# Detect cycle in f(n) modulo MOD
def detect_cycle():
    seen = {}
    f = [1, 1, 2]
    i = 3
    while True:
        next_f = (f[-1] + f[-2] + f[-3]) % MOD
        if next_f in seen:
            cycle_start = seen[next_f]
            return f[:cycle_start], f[cycle_start:]
        seen[next_f] = i
        f.append(next_f)
        i += 1

# Compute S(L) mod MOD
def compute_S(L):
    prefix, cycle = detect_cycle()
    prefix_sum = sum(mod_exp(x, 3, MOD) for x in prefix) % MOD
    cycle_sum = sum(mod_exp(x, 3, MOD) for x in cycle) % MOD
    
    prefix_len = len(prefix)
    cycle_len = len(cycle)
    
    if L <= prefix_len:
        return sum(mod_exp(prefix[i], 3, MOD) for i in range(L)) % MOD
    
    total_sum = prefix_sum
    remaining = L - prefix_len
    
    # Full cycles
    full_cycles = remaining // cycle_len
    total_sum += (full_cycles * cycle_sum) % MOD
    
    # Partial cycle
    partial_len = remaining % cycle_len
    total_sum += sum(mod_exp(cycle[i], 3, MOD) for i in range(partial_len)) % MOD
    
    return total_sum % MOD

# Compute S(10^14)
L = 10**14
result = compute_S(L)
print(result)
