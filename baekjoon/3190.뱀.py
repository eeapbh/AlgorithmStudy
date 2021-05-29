import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**9)

n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
m = int(input())
d = [input().split() for _ in range(m)]
arr = [[0]*n for _ in range(n)]
# print(d)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
idx = 0
sx = sy = 0
cnt = 0
arr[0][0] = 0
ans = 0
for a in apples:
    arr[a[0]-1][a[1]-1] = -1

# print(arr)
def dfs(sx, sy, ex, ey, idx, cnt, tail):
    global ans
    for i in d:
        if int(i[0]) == cnt:
            if i[1] == 'L':
                idx = (idx + 3) % 4
                break
            elif i[1] == 'D':
                idx = (idx + 1) % 4
                break
    nx = sx + dx[idx]
    ny = sy + dy[idx]
    if nx < 0 or nx >=n or ny < 0 or ny >= n:
        # 벽을 만났을떄
        ans = cnt
        return cnt + 1
    else:
        if arr[nx][ny] > 0:
            # 자기 몸을 만났을때
            ans = cnt
            return cnt + 1
        elif arr[nx][ny] == -1:
            # 사과를 먹었을 때
            arr[nx][ny] = cnt+1
            sx = nx
            sy = ny
            return dfs(sx, sy, ex, ey, idx, cnt+1, tail)
        elif arr[nx][ny] == 0:
            # 사과가없을때
            arr[nx][ny] = cnt+1
            for i in range(4):
                tx = ex + dx[i]
                ty = ey + dy[i]
                if 0<=tx < n and 0<=ty < n and arr[tx][ty] == tail + 1:
                    arr[ex][ey] = 0
                    ex = tx
                    ey = ty
                    break
            sx = nx
            sy = ny

            return dfs(sx, sy, ex, ey, idx, cnt+1, tail+1)

# dfs(0, 0, 0, 0, 0, 0, 0)
print(dfs(0, 0, 0, 0, 0, 0, 0))
# print(ans + 1)
