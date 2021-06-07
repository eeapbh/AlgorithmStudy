n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
tmp = []
for i in range(n-1):
    if arr[i] * (n-i) > arr[i+1] * (n-i-1):
        tmp.append(arr[i] * (n - i))
tmp.append(arr[n-1])
print(max(tmp))