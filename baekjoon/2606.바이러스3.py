from collections import deque

c = int(input())
n = int(input())
arr = [[0]*(c + 1) for  _ in range(c + 1)]
visit = []
for _ in range(n):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1


def dfs(x):
    visit.append(x)
    for i in range(1, c + 1):
        if arr[x][i] == 1 and i not in visit:
            dfs(i)
def bfs():
    q = deque()
    q.append(1)
    visit.append(1)
    while q:
        x = q.popleft()
        for i in range(1, c + 1):
            if arr[x][i] == 1 and i not in visit:
                q.append(i)
                visit.append(i)

bfs()
print(len(visit) - 1)
