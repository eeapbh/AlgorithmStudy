import sys
import heapq
n, k = map(int, sys.stdin.readline().split())
jew = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

heapq.heapify(jew)

bag = [int(sys.stdin.readline()) for _ in range(k)]
bag.sort()

ans = 0
tmp = []
for b in bag:
    while jew and jew[0][0] <= b:
        heapq.heappush(tmp, -heapq.heappop(jew)[1])

    if tmp:
        ans -= heapq.heappop(tmp)
    elif not jew:
        break
print(ans)



