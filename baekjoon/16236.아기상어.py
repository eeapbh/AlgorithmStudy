n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
baby = 2

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            sx, sy = i, j
