board =[[0,0,0,0,2,0,0,0,0,0],
        [0,0,1,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,0,1,0],
        [0,0,1,1,1,1,1,0,0,0],
        [0,0,0,0,3,0,0,0,1,0]]
c = 2

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(board, c):
    sx, sy = 0, 0
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                sx, sy = i, j
    q = deque()
    rs = []
    visit = [(sx, sy)]
    q.append((sx, sy, 0))
    while q:
        cx, cy, cc = q.popleft()
        if board[cx][cy] == 3:
            rs.append(cc)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m and (nx, ny) not in visit:
                if board[nx][ny] == 0:
                    q.append((nx, ny, cc + 1))
                    visit.append((nx, ny))
                elif board[nx][ny] == 1:
                    q.append((nx, ny, cc + 1 + c))
                    visit.append((nx, ny))
                elif board[nx][ny] == 3:
                    q.append((nx, ny, cc + 1))
    return min(rs)
print(solution(board, c))
