import heapq
n = int(input())
arr = [int(input()) for _ in range(n)]

ans = 0
heapq.heapify(arr)
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    ans += a + b
    heapq.heappush(arr, a+b)


print(ans)