import heapq
import sys
V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]
INF = 1e9
distance = [INF]*(V+1)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        d, n = heapq.heappop(q)

        if distance[n] < d:
            continue

        for w, next in graph[n]:
            if distance[next] > d + w:
                distance[next] = d + w
                heapq.heappush(q, (d+w, next))
dijkstra(start)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

