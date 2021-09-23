board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
from copy import deepcopy
def bfs(board, loc):
    n = len(board)
    m = len(board[0])
    q = deque()
    visit = deepcopy(board)
    # print(visit)
    q.append((loc[0], loc[1], loc[2], loc[3], 0, visit))
    save = []
    while q:

        ax, ay, bx, by, cnt, tmpboard = q.popleft()
        # print([ax, ay], [bx, by], cnt, cboard)
        cboard = deepcopy(tmpboard)
        if (ax, ay) == (0, 0) and (bx, by) == (0, 1):

            print(cboard, cnt)

        if cnt % 2 == 0:

            for i in range(4):
                nx = ax + dx[i]
                ny = ay + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if cboard[nx][ny] == 1:
                        cboard[ax][ay] = 0
                        q.append((nx, ny, bx, by, cnt + 1, cboard))

        else:

            for i in range(4):
                nx = bx + dx[i]
                ny = by + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if cboard[nx][ny] == 1:
                        cboard[bx][by] = 0
                        q.append((ax, ay, nx, ny, cnt + 1, cboard))


    return cnt

def solution(board, aloc, bloc):
    loc = aloc + bloc
    answer = (bfs(board, loc))
    return answer

print(solution(board, aloc, bloc))