from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x):
    visit1.append(x)
    for i in range(n+1):
        if arr[x][i] == 1 and i not in visit1:
            dfs(i)
def bfs(x):
    q = deque()
    q.append(x)
    visit2.append(x)
    while q:
        x = q.popleft()

        for i in range(n + 1):
            if arr[x][i] == 1 and i not in visit2:
                visit2.append(i)
                q.append(i)



n, m, v = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1
visit1 = []
visit2 = []
rs1 = []
dfs(v)
bfs(v)
print(*visit1)
print(*visit2)



