import sys
from collections import Counter
input = sys.stdin.readline
MOD = 998244353

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    freq = list(Counter(a).values())

    mx = max(freq)
    dp = [0] * (n + 1)
    dp[0] = 1
    print(f'{mx=}')

    # editorial transition: for each color frequency c
    for c in freq:
        # iterate down to avoid reuse in same iteration
        for j in range(n, c - 1, -1):
            dp[j] = (dp[j] + c * dp[j - c]) % MOD

    # sum all dp[j] where j >= mx
    print(*dp)
    ans = sum(dp[mx:]) % MOD
    print(ans)
