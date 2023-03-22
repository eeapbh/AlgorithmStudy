from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(arr)
def bfs(x, y):
    q = deque()
    q.append((x, y, 1))
    visit = []
    visit.append((x, y))
    while q:
        x, y, c = q.popleft()
        if x == n-1 and y == m-1:
            print(c)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if (nx, ny) not in visit and arr[nx][ny] == 1:
                    q.append((nx, ny, c + 1))
                    visit.append((nx, ny))
bfs(0, 0)
