from collections import deque
t = int(input())
def bfs():
    q = deque()
    q.append((hx, hy))
    while q:
        x, y = q.popleft()
        if abs(x - fx) + abs(y - fy) <= 1000:
            print('happy')
            return
        for i in range(n):
            if visit[i] == 0:
                if abs(conve[i][0] - x) + abs(conve[i][1] - y) <= 1000:
                    visit[i] = 1
                    q.append((conve[i][0], conve[i][1]))
    print('sad')
    return

for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    conve = []
    visit = [0]*(n)
    
    for _ in range(n):
        a, b = map(int, input().split())
        conve.append((a, b))
    fx, fy = map(int, input().split())
    bfs()