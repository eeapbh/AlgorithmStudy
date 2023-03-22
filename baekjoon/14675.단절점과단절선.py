n = int(input())
arr = [[0]*(n + 1) for _ in range(n + 1)]
save = []
for _ in range(n):
    a, b = map(int, input().split())
    save.append((a, b))
    arr[a][b] = 1
    arr[b][a] = 1
q = int(input())
for _ in range(q):
    t, k = map(int, input())
    visit = []
    if t == 1:
        # k 번 정점에 대한 질의
        for i in range(1, n + 1):
            if i != k and i not in visit:
                for j in range(1, n + 1):
                    if arr[i][j] == 1:



    else:


