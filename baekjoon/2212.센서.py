n = int(input())
k = int(input())
arr = list(map(int, input().split()))

if k >= n:
    print(0)
else:
    arr.sort()
    tmp = []
    for i in range(1, n):
        tmp.append((arr[i] - arr[i-1]))
    tmp.sort()
    for i in range(k-1):
        tmp.pop()
    print(sum(tmp))