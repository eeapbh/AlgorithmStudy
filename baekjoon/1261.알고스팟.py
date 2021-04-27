n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[-1]*n for _ in range(m)]
visit[0][0] = 0
q = deque()
q.append((0, 0))
while q:
    Cx, Cy = q.popleft()
    for i in range(4):
        nx = Cx + dx[i]
        ny = Cy + dy[i]
        if 0<=nx<m and 0<=ny<n:
            if visit[nx][ny] == -1:
                if arr[nx][ny] == '0':
                    q.appendleft((nx, ny))
                    visit[nx][ny] = visit[Cx][Cy]
                elif arr[nx][ny] == '1':
                    q.append((nx, ny))
                    visit[nx][ny] = visit[Cx][Cy] + 1
print(visit[m-1][n-1])
