import sys
sys.setrecursionlimit(1000000)
t = int(input())
def dfs(x):
    visit[x] = 1
    if visit[arr[x]] == 1:
        return
    dfs(arr[x])
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)

    visit = [0]*(n+1)
    cnt = 0
    for i in range(1, n+1):
        if visit[i] == 0:
            dfs(i)
            cnt += 1
    print(cnt)