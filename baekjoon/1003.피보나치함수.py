t = int(input())
dp = [(1, 0), (0, 1), (1, 1), (1, 2)] + [(0, 0) for _ in range(37)]
for _ in range(t):
    n = int(input())
    for i in range(4, n+1):
        dp[i] = (dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1])
    print(*dp[n])

