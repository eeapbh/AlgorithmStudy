from collections import deque
import sys
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
ans = [0]*(n+1)
def bfs():

    q = deque()
    q.append(1)
    visit = [0]*(n+1)
    while q:
        x = q.popleft()

        for i in tree[x]:
            if visit[i] == 0:
                ans[i] = x
                q.append(i)
                visit[i] = 1

bfs()
print(tree)
for i in range(2, n+1):
    print(ans[i])
