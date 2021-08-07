import sys

sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n+1)]
visit = [0]*(n+1)
def dfs(v):
    visit[v] = 1
    for a in arr[v]:
        if not visit[a]:
            dfs(a)
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    arr[s].append(e)
    arr[e].append(s)

cnt = 0
for i in range(1, n+1):
    if not visit[i]:
        dfs(i)
        cnt += 1
print(cnt)