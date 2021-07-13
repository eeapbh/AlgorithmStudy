n, m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(m):
    arr.sort()
    a = arr[0]
    b = arr[1]
    arr[0] = a + b
    arr[1] = a + b
print(sum(arr))