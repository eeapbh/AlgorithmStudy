import sys
sys.setrecursionlimit(100000)
n = int(input())

def dfs(x, c):
    visit[x] = 1
    level[x] = c
    for i in tree[x]:
        if not visit[i]:
            parent[i] = x
            dfs(i, c + 1)

def lca(a, b):
    while level[a] != level[b]:
        if level[a] > level[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0]*(n + 1)
level = [0]*(n + 1)
visit = [0]*(n +1)

dfs(1, 0)

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))