import sys
from collections import deque
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]

def bfs(x):
    visit = [0]*(n + 1)
    q = deque()
    q.append((1, 0))
    visit[x] = 1
    ans = 0
    while q:
        x, d = q.popleft()
        if x != 1 and len(tree[x]) == 1:
            ans += d
        for t in tree[x]:
            if visit[t] == 0:
                q.append((t, d + 1))
                visit[t] = 1
    return ans


for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())

    tree[a].append(b)
    tree[b].append(a)


a = bfs(1)
if a % 2 == 0:
    print('No')
else:
    print('Yes')