import sys
import heapq

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[0], x[1]))

heapq.heapify(arr)
tmp = []
for i in range(n):
    if len(tmp) > 0 and tmp[0] <= arr[i][0]:
        heapq.heappop(tmp)
    heapq.heappush(tmp, arr[i][1])
print(len(tmp))