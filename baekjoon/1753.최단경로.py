import sys
import heapq
sys.stdin = open('input.txt')

V, E = map(int, input().split())
k = int(input())
INF = sys.maxsize

graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        d, now = heapq.heappop(q)

        if distance[now] < d:
            continue

        for w, next_node in graph[now]:
            next_w = w + d

            if next_w < distance[next_node]:
                distance[next_node] = next_w
                heapq.heappush(q, (next_w, next_node))
Dijkstra(k)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:print(distance[i])
