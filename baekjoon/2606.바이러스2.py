n = int(input())
m = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1



def bfs(x):
    q = []
    q.append(x)
    while q:
        cx = q.pop(0)
        visit[cx] = 1
        for i in range(1, n+1):
            if arr[cx][i] == 1 and visit[i] == 0:
                q.append(i)

    return sum(visit) - 1

print(bfs(1))