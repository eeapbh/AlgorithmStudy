board =[ [0,0,0,0,2,0,0,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,0,1,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,3,0,0,0,1,0]]
c = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = []
rs = []
def dfs(x, y, cc, visit, board, n, m, c):
    global rs
    visit.append((x, y))
    if board[x][y] == 3:
        print(cc)
        return cc
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx < n and 0<=ny < m and (nx, ny) not in visit:
            if board[nx][ny] == 0:

                dfs(nx, ny, cc + 1, visit, board, n, m, c)
            elif board[nx][ny] == 1:

                dfs(nx, ny, cc + 1 + c, visit, board, n, m, c)
            elif board[nx][ny] == 3:
                rs.append(cc + 1)



def solution(board, c):
    answer = 0
    sx, sy, gx, gy = 0, 0, 0, 0
    n = len(board)
    m = len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                sx, sy = i, j
            if board[i][j] == 3:
                gx, gy = i, j

    dfs(sx, sy, 0, visit, board, n, m, c)
    return rs
print(solution(board, c))