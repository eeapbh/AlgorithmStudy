n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
ans = 0
for i in range(n):
    if arr[i] - i > 0:
        ans += arr[i] - i
print(ans)
