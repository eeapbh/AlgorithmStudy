import heapq
import sys
n = int(sys.stdin.readline())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
q = []
for i in arr:
    heapq.heappush(q, i[1])
    if i[0] < len(q):
        heapq.heappop(q)

print(sum(q))
