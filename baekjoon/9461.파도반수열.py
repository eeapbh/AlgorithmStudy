dp = [0, 1, 1, 1, 2, 2 ] + [0]*95
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])
