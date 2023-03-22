arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
def solution(arrows):
    x = 5
    y = 5
    arr = [[0]*11 for _ in range(11)]
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    for a in arrows:
        nx = x + dx[a]
        ny = y + dy[a]
        arr[nx][ny] = 1
        x = nx
        y = ny
    answer = 0
    for a in arr:
        print(a)
    return answer

solution(arrows)