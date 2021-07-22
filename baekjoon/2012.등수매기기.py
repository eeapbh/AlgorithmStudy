import sys

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()
ans = 0
for i in range(n):
    ans += abs(i + 1 - arr[i])
print(ans)
