import sys
from collections import deque
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]
check = [0 for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)
    tree[e].append(s)

def bfs():
    q = deque()
    q.append(1)
    while q:
        p = q.popleft()
        for i in tree[p]:
            if not check[i]:
                parent[i] = p
                check[i] = 1
                q.append(i)
bfs()

for i in range(2, n+1):
    print(parent[i])
