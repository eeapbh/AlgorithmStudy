import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))


def bfs(x, t):
    q = deque()
    q.append(x)
    dist = [-1 for _ in range(n+1)]
    dist[x] = 0
    while q:
        x = q.popleft()
        for nx, w in tree[x]:
            if dist[nx] == -1:
               dist[nx] = dist[x] + w
               q.append(nx)

    if t == 1:
        return dist.index(max(dist))
    else:
        return max(dist)

print(bfs(bfs(1, 1), 2))