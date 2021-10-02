from collections import deque

f, s, g, u, d = map(int, input().split())

def bfs():
    q = deque()
    q.append((s, 0))
    visit = [0]*(f+1)
    visit[s] = 1
    while q:
        ns, nc = q.popleft()
        if ns == g:
            return nc
        if ns + u <= f and visit[ns+u] == 0:
            q.append((ns+u, nc + 1))
            visit[ns+u] = 1
        if ns - d >= 1 and visit[ns-d] == 0:
            q.append((ns-d, nc + 1))
            visit[ns-d] = 1
    return 'use the stairs'



print(bfs())
