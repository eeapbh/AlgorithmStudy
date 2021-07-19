import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0

    M = arr[-1]
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] <= M:
            ans += M - arr[i]

        else:
            M = arr[i]
    print(ans)

