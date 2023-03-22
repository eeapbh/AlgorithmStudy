vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
from collections import deque
def bfs(x, arr, visit, n):
    q = deque()
    q.append((x, 0))
    visit[x] = 1
    save = []
    while q:
        x, c = q.popleft()
        save.append((x, c))
        for i in arr[x]:
            if visit[i] == 0:
                q.append((i, c + 1))
                visit[i] = 1
    return save, c

def solution(n, vertex):
    answer = 0
    arr = [[] for _ in range(n + 1)]
    visit = [0]*(n + 1)
    for s, e in vertex:
        arr[s].append(e)
        arr[e].append(s)

    tmp, c = bfs(1, arr, visit, n)
    print(arr)

    for t in tmp:
        if t[1] == c:
            answer += 1

    return answer

print(solution(n, vertex))