import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    arr.sort(key=lambda x:x[0])

    min = arr[0][1]
    cnt = 1
    for i in range(1, n):
        if arr[i][1] <= min:
            min = arr[i][1]
            cnt += 1
    print(cnt)
