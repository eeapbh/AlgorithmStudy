from collections import deque
n = int(input())
a, b = map(int, input().split())
m = int(input())
tree = [[] for _ in range(n+1)]
ans = [0 for _ in range(n+1)]

def bfs(a, b):
    q = deque()
    q.append((a, 0))
    visit = [0]*(n+1)

    while q:
        x, c = q.popleft()
        if x == b:
            return c
        if not visit[x]:
            visit[x] = 1
            for i in tree[x]:
                if not visit[i]:
                    q.append((i, c+1))
    return -1
for _ in range(m):
    p, c = map(int, input().split())
    tree[c].append(p)
    tree[p].append(c)
print(bfs(a, b))

