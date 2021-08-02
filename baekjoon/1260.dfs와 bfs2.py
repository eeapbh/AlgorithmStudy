import sys
sys.stdin = open('input.txt', 'r')
n, m, v = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n + 1)]

for i in range(m):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1


visit = [0]*(n+1)
def dfs(x):
    print(x, end=' ')
    visit[x] = 1
    for i in range(n + 1):
        if arr[x][i] == 1 and visit[i] == 0:
            dfs(i)

visit2 = [0]*(n+1)
def bfs(x):
    q = []
    q.append(x)
    visit2[x] = 1
    while q:
        v = q.pop(0)
        print(v, end= ' ')
        for i in range(n + 1):
            if visit2[i] == 0 and arr[v][i] == 1:
                q.append(i)
                visit2[i] = 1
dfs(v)
print()
bfs(v)
