n = 3
start = 1
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]
result = 5

def dfs(x):
    if x in traps:
        for i in range(1, n+1):
            for j in range(1, n+1)
                arr[i]

def solution(n, start, end, roads, traps):
    arr = [[0]*(n+1) for _ in range(n + 1)]
    for r in roads:
        s = r[0]
        e = r[1]
        arr[s][e] =r[2]

    for i in range(1, n+1):
        if arr[start][i] != 0:
            dfs(i)
    print(arr)
    answer = 0
    return answer

solution(n, start, end, roads, traps)