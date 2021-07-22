n, k = map(int, input().split())
arr = [1]*n
while 1:
    arr.sort(reverse=True)
    tmp = []
    if arr.count(0) <= k:
        break
    for i in range(n-2):
        if arr[i] == arr[i + 1]:
            tmp.append(arr[i] + arr[i + 1])
            arr[i + 1] = 0

