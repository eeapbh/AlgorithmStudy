import heapq
import sys
n = int(input())
m = int(input())
INF = 1e9
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    s, e, cost = map(int, sys.stdin.readline().split())
    graph[s].append((cost, e))
start, end = map(int, input().split())


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        d, n = heapq.heappop(q)

        if distance[n] < d:
            continue
        for w, next in graph[n]:
            if w + d < distance[next]:
                distance[next] = w + d
                heapq.heappush(q, (w+d, next))

dijkstra(start)

print(distance[end])
