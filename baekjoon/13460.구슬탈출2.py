import sys

sys.stdin = open('input.txt', 'r')
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = []
visit = []

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                rx, ry = i, j
            elif arr[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visit.append((rx, ry, bx, by))

def move(x, y, dx, dy):
    cnt = 0

    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    init()  # 시작 조건
    while q:  # BFS : queue 기준
        rx, ry, bx, by, depth = q.pop(0)
        if depth > 10:  # 실패 조건
            break
        for i in range(4):  # 4방향 이동 시도
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  # Red
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])  # Blue
            if arr[nbx][nby] != 'O':  # 실패 조건이 아니면
                if arr[nrx][nry] == 'O':  # 성공 조건
                    print(depth)
                    return
                if nrx == nbx and nry == nby:  # 겹쳤을 때
                    if rcnt > bcnt:  # 이동거리가 많은 것을
                        nrx -= dx[i]  # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # breadth 탐색 후, 탐사 여부 체크
                if not (nrx, nry, nbx, nby) in visit:
                    visit.append((nrx, nry, nbx, nby))
                    # 다음 depth의 breadth 탐색 위한 queue
                    q.append((nrx, nry, nbx, nby, depth + 1))
    print(-1)  # 실패 시


bfs()