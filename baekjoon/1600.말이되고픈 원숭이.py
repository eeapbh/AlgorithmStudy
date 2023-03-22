from collections import deque
import sys
hx = [-1, -2, -2, -1, 1, 2, 2, 1]
hy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(k):
    q = deque()
    q.append((0, 0, 0, k))
    visit = []

    while q:
        x, y, c, z = q.popleft()
        if x == h - 1 and y == w - 1:
            print(c)
            return
        visit.append((x, y))
        if z > 0:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if arr[nx][ny] == 0 and (nx, ny) not in visit:
                        q.append((nx, ny, c + 1, z - 1))

        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if arr[nx][ny] == 0 and (nx, ny) not in visit:
                        q.append((nx, ny, c + 1, z))

    print('-1')
    return
k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
bfs(k)