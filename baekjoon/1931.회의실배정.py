import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(arr)
arr.sort(key=lambda x:(x[1], x[0]))
e = arr[0][1]
cnt = 1
for i in range(1, n):
    if arr[i][0] >= e:
        cnt += 1
        e = arr[i][1]
# print(arr)
print(cnt)
