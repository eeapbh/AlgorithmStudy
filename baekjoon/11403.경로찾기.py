n = int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
    i, j, c = map(int, input().split())
    arr[i][j] = c
