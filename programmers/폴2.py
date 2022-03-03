dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    q = [[x, y, 0]]
    visit = [[x, y]]
    while q:
        cx, cy, cc = q.pop(0)
        if [cx+1, cy+1] in bus_stop:
            print(cc)
            return cc
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<n and [nx, ny] not in visit:
                q.append([nx, ny, cc + 1])
                visit.append([nx, ny])


def solution(n, bus_stop):
    answer = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            answer[i][j] = bfs(i, j)

    return answer


n = 3
bus_stop = [[1,2],[3,3]]
print(solution(n, bus_stop))

