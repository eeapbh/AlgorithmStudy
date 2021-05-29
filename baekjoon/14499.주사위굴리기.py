n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dice = [0]*6
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for  i in range(k):
    nx = x + dx[order[i] - 1]
    ny = y + dy[order[i] - 1]
    if 0<=nx <n and 0<=ny < m:

        if order[i] - 1 == 0:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif order[i] - 1== 1:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif order[i] - 1 == 2:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        else:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        if arr[nx][ny] == 0:
            arr[nx][ny] = dice[5]
        else:
            dice[5] = arr[nx][ny]
            arr[nx][ny] = 0
        print(dice[0])
        x = nx
        y = ny
