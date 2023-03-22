from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
save1 = []
save2 = []
def dfs(x):
    save1.append(x)
    for i in range(1, n+1):
        if arr[x][i] == 1 and i not in save1:
            dfs(i)

def bfs(x):
    q = deque()
    q.append(x)
    save2.append(x)
    while q:
        x = q.popleft()
        for i in range(1, n+1):
            if arr[x][i] == 1 and i not in save2:
                save2.append(i)
                q.append(i)


    for i in range(1, n+1):
        save = []
        if arr[x][i] == 1:
            save.append(i)



n, m, v = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]

visit = []
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
# print(arr)
dfs(v)
print(*save1)
bfs(v)
print(*save2)