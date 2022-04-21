import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]
def dfs(x):
    visit[x] = 1
    if len(tree[x]) == 0:
        dp[x][1] = 1
        dp[x][0] = 0
    for i in tree[x]:
        if visit[i] == 0:
            dfs(i)
            dp[x][1] += min(dp[i][0], dp[i][1])
            dp[x][0] += dp[i][1]
    dp[x][1] += 1
dfs(1)
print(min(dp[1][0], dp[1][1]))
