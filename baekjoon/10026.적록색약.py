import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit1 = []

def dfsR(x, y):
    visit1.append((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] == 'R' and (nx, ny) not in visit1:
                dfsR(nx, ny)

def dfsG(x, y):
    visit1.append((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] == 'G' and (nx, ny) not in visit1:
                dfsG(nx, ny)

def dfsB(x, y):
    visit1.append((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] == 'B' and (nx, ny) not in visit1:
                dfsB(nx, ny)


def dfsRG(x, y):
    visit1.append((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and (nx, ny) not in visit1:
            if arr[nx][ny] == 'R' or arr[nx][ny] == 'G':
                dfsRG(nx, ny)
cnt1 = 0
cnt2 = 0
cntB = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R' and (i, j) not in visit1:
            dfsR(i, j)
            cnt1 += 1
        if arr[i][j] == 'G' and (i, j) not in visit1:
            dfsG(i, j)
            cnt1 += 1
        if arr[i][j] == 'B' and (i, j) not in visit1:
            dfsB(i, j)
            cntB += 1
visit1 = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R' or arr[i][j] == 'G':
            if (i, j) not in visit1:
                dfsRG(i, j)
                cnt2 += 1
print(cnt1+cntB, cnt2+cntB)
