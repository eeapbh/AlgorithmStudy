n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
ans = arr[0] + arr[1]
arr.pop(0)
arr.pop(0)
print(arr)
while len(arr):
    ans = 2 * ans + arr.pop(0)
print(ans)
