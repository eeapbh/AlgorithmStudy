while 1:
    n = int(input())
    if n == 0:
        break
    arr = [1]* (2*n +1)
    cnt = 0
    for i in range(2, int(2*n ** 0.5)+1):
        if arr[i]:
            for j in range(2*i, 2 *n +1, i):
                arr[j] = 0
    print(sum(arr[n+1:2*n+1]))
