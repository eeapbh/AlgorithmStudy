t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    arr = [[]]
    for i in range(1, n+1):
        arr[0].append(i)
    for _ in range(k):
        arr.append([0]*n)

    for i in range(1, k+1):
        for j in range(n):
            arr[i][j] = sum(arr[i-1][:j+1])
    print(arr[k][n-1])


