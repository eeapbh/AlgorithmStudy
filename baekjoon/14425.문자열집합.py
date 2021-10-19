import sys
n, m = map(int, input().split())
arr1 = [sys.stdin.readline() for _ in range(n)]
cnt = 0
for _ in range(m):
    word = input()
    if word in arr1:
        cnt += 1
print(cnt)