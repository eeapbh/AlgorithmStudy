import sys
sys.stdin = open('input.txt', 'r')

arr = [list(map(int, input().split())) for _ in range(19)]
# 아래 아랫대각 오른쪽 윗대각
dx = [1, 1, 0, -1]
dy = [0, 1, 1, 1]
def check(num, x, y, cnt, idx):
    if cnt == 5:
        if arr[x+dx[idx]][y+dy[idx]] != num and arr[x-5*dx[idx]][y-5*dy[idx]] != num:
            return 1

    for i in range(4):
        if cnt > 1 and idx != i:
            continue
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<19 and 0<=ny<19:
            if arr[nx][ny] == num:
                return check(num, nx, ny, cnt+1, i)


def ans():
    for i in range(19):
        for j in range(19):
            if arr[j][i] != 0:
                rs = check(arr[j][i], j, i, 1, 0)
                if rs == 1:
                    return arr[j][i], j+1, i+1
    return 0, 0, 0
num, x, y = ans()
if num == 0:
    print(num)
else:
    print(num)
    print(x, y)