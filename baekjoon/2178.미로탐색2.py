import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dis = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visit = []
def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and (nx, ny) not in visit:
                q.append((nx, ny))
                visit.append((nx, ny))
                dis[nx][ny] = dis[cx][cy] + 1
                if nx == n-1 and ny == m-1:
                    return dis[nx][ny] + 1

print(bfs())





