import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visit = []
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
bx = by = rx = ry = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'B':
            bx, by = i, j
        if arr[i][j] == 'R':
            rx, ry = i, j

    visit.append((bx, by, rx, ry))
def move(x, y, dx, dy):
    cnt = 0
    while arr[x+dx][y+dy] != '#' or arr[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(bx, by, rx, ry):
    q = deque()
    q.append((bx, by, rx, ry, 1))
    while q:
        bx, by, rx, ry, c = q.popleft()
        if c > 10:
            print(-1)
            return

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if arr[nbx][nby] != 'O':
                if arr[nrx][nry] == 'O':
                    print(c)
                    break
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not (nbx, nby, nrx, nry) in visit:
                    visit.append((nbx, nby, nrx, nry))
                    q.append((nbx, nby, nrx, nry, c + 1))

bfs(bx, by, rx, ry)