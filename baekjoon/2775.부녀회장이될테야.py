t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    arr = [[]]
    for i in range(1, n+1):
        arr[0].append(i)
    for i in range(1, k):
        arr.append([])
    # print(arr)
    for i in range(n):
        arr[1].append(sum(arr[0][:i+1]))
    # print(1111, arr)
    arr.append([0]*n)
    for i in range(2, k+1):
        for j in range(n):
            arr[i][j] = sum(arr[i-1][:j]) + (2*arr[i-1][j])
        print(2222, arr)
# print(3333, arr)
    print(arr[k][n-1])



