from collections import deque
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    a = list(map(int, input().split()))

    tree[a[0]].append(a[1:-1])

def bfs(x, t):
    q = deque()
    q.append(x)
    dist = [-1]*(n+1)

    dist[x] = 0
    while q:
        x = q.popleft()
        for i in range(0, len(tree[x][0])-1, 2):
            nx, w = tree[x][0][i], tree[x][0][i+1]
            if dist[nx] == -1:
                dist[nx] = dist[x] + w
                q.append(nx)


    if t == 1:
        return dist.index(max(dist))
    else:
        return max(dist)

print(bfs(bfs(1, 1), 2))