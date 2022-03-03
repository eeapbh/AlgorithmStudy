board =[ [0,0,0,0,2,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,0,1,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,3,0,0,0,1,0]]
c = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = len(board)
m = len(board[0])

def bfs(x, y, gx, gy):
    q = []
    visit = [(x, y)]
    q.append((x, y, 0))
    rs = []
    while q:
        cx, cy, cc = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx <n and 0<=ny < m and (nx, ny) not in visit:
                if board[nx][ny] == 0:
                    q.append((nx, ny, cc + 1))
                    visit.append((nx, ny))

                elif board[nx][ny] == 1:
                    q.append((nx, ny, cc + 1 + c))
                    visit.append((nx, ny))

                if nx == gx and ny == gy:
                    return dis[nx][ny] + 1, 'zz'
    return dis[gx][gy] + 1, 'ㅋㅋ'

def solution(board, c):
    sx, sy, gx, gy = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                sx, sy = i, j
            if board[i][j] == 3:
                gx, gy = i, j
    print(bfs(sx, sy, gx, gy))
    answer = 0

    return answer


print(solution(board, c))
