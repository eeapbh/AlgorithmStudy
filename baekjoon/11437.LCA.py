import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
def bfs(x):
    visit = [0]*(n + 1)
    q = deque()
    q.append((x, 0))
    visit[x] = 1
    while q:
        x, d = q.popleft()
        depth[x] = d

        for t in tree[x]:
            if visit[t] == 0:
                q.append((t, d + 1))
                visit[t] = 1
                parent[t] = x
    print(depth)
    print(parent)
def dfs(x, d):
    for t in tree[x]:
        if depth[t] == d:
            return t
        else:
            dfs(t, d)

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
print(tree)
parent = [0]*(n + 1)
depth = [0]*(n + 1)
bfs(1)


m = int(input())

for j in range(m):
    c, d = map(int, input().split())
    while 1:
        if c == d:
            print(c)
        if depth[c] == depth[d]:
            tmp1, tmp2 = 0, 0
            for t in tree[c]:
                if depth[t] == depth[c] - 1:
                    tmp1 = t
            for t in tree[d]:
                if depth[t] == depth[d] - 1:
                    tmp2 = t
            if tmp1 == tmp2:
                print(tmp1)
                break
            else:
                c = tmp1
                d = tmp2
        else:
            if depth[c] > depth[d]:
                c = dfs(c, depth[d])

            elif depth[c] < depth[d]:
                d = dfs(d, depth[c])





