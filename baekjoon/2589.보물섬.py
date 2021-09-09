from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline()) for _ in range(n)]
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q.append((x, y, 0))
    visit = [[0] * m for _ in range(n)]


    while q:
        x, y, c = q.popleft()
        visit[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == 'L' and visit[nx][ny] == 0:
                    q.append((nx, ny, c + 1))
                    visit[nx][ny] = 1 #왜 이거 안넣으면 메모리 추가가되는거지?!!?!?!?!?!?!?!?!?!?!?!!?

    return c

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            ans = max(ans, bfs(i, j))
print(ans)