import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visit.append((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and (nx, ny) not in visit:
            if arr[nx][ny] == 0:
                dfs(nx, ny)
            if arr[nx][ny] == 1:
                save.add((nx, ny))


cnt = 0
ans = 0

while 1:
    tmp = ans
    ans = 0
    cnt += 1
    for i in arr:
        ans += sum(i)
    if ans == 0:
        break
    visit = []
    save = set()
    dfs(0, 0)
    for s in save:
        arr[s[0]][s[1]] = 0

print(cnt-1)
print(tmp)