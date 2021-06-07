n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
for i in range(n):
    if arr[i] > k:
        arr = arr[0:i]
        break
arr.sort(reverse=True)
ans = 0
for i in range(len(arr)):

    ans += k // arr[i]
    k = k % arr[i]
    if k == 0:
        break
print(ans)