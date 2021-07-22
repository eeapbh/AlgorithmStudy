import sys

sys.stdin = open('input.txt', 'r')
import heapq
n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append([-a, a])
heapq.heapify(arr)

ans = 0

while 1:
    if len(arr) == 0:
        print(ans)
        break
    tmp = []
    if len(arr) < 3:
        while 1:
            a, b = heapq.heappop(arr)
            ans += b
            if len(arr) == 0:
                break
    if len(arr) == 0:
        print(ans)
        break

    while len(tmp) < 3:
        a, b = heapq.heappop(arr)
        tmp.append(b)
    ans += tmp[0] + tmp[1]
