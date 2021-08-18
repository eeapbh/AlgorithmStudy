# 아기 상어 처음 크기 2
# 아기상어는 자신의 크기와 같은수의 물고기를 먹을대 마다 1씩커짐
from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
trg = 0
save = [0]*10
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x, y = i, j
            arr[i][j] = 0
        if arr[i][j] !=9 and arr[i][j] !=0:
            trg += 1
            save[arr[i][j]] += 1
print(trg)

def bfs(bx, by, bs, bc, a, trg):
    q = deque()
    q.append((bx, by, bs, bc, a))
    if trg == 0:
        return 0
    while q:

        x, y, s, c, ans = q.popleft()

        # print(x, y, ans)
        save.append(c)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] <= s: # 같으면 지나갈수는 잇다
                    if arr[nx][ny] < s and arr[nx][ny] != 0: # 작으면 먹는다.

                        # 빈칸이 아니면 먹는다는것
                        trg -=1
                        if trg == 0:
                            return ans+1, '킼'
                        arr[nx][ny] = 0
                        c += 1
                        if s == c:
                            s += 1
                            c = 0
                        q.append((nx, ny, s, c, ans + 1))
                    else:
                        q.append((nx, ny, s, c, ans + 1))
    return ans


print(bfs(x, y, 2, 0, 0, trg))