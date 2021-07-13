t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    for j in range(2, n):
        ans = max(arr[j] - arr[j-2], ans)
    print(ans)
