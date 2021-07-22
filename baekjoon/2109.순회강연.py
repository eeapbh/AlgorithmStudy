import heapq
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[0]))
q = []
for i in arr:
    heapq.heappush(q, i[0])
    if i[1] < len(q):
        heapq.heappop(q)

print(sum(q))
