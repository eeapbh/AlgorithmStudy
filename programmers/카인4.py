n = 6
paths =[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates =[1, 3]
summits =[5]


def solution(n, paths, gates, summits):
    answer = []
    arr = [[0]*(n + 1) for _ in range(n + 1)]
    for s, e, v in paths:
        arr[s][e] = v
        arr[e][s] = v
    save = []

    intensity = -1
    def dfs(x, intensity, visit):

        if x in gates:

            save.append([s, intensity])

            return
        for i in range(1, n+1):
            if x == s:
                visit = [0]*(n + 1)
                visit[s] = 1
            if visit[i] == 0 and arr[x][i] != 0:
                if i in summits and i != s:
                    return
                # if arr[x][i] > intensity:
                #     intensity = arr[x][i]
                visit[i] = 1
                dfs(i, max(intensity, arr[x][i]), visit)

    for s in summits:
        visit = [0] * (n + 1)
        intensity = -1
        visit[s] = 1
        dfs(s, intensity, visit)
    save.sort(key=lambda x:x[1])

    return save[0]

print(solution(n, paths, gates, summits))