from collections import deque
import sys
def bfs(x):
    q = deque()
    q.append((x, 1))
    visit[x] = 1
    while q:
        x, c = q.popleft()
        for i in arr[x]:
            if visit[i] == 0:
                visit[i] = -c
                q.append((i, -c))
            else:
                if visit[i] == c:
                    return -1

t = int(sys.stdin.readline())
for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(v+1)]
    visit = [0]*(v+1)
    trg = 0
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)
    for i in range(1, v+1):
        if visit[i] == 0:
            trg = bfs(i)
            if trg == -1:
                print('NO')
                break
    else:
        print('YES')