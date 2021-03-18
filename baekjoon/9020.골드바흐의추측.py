t = int(input())
arr = [0, 0] + [1]*10000
for i in range(2, int(10000**0.5)+1):
    if arr[i]:
        for j in range(2*i, 10000, i):
            arr[j] = 0

for _ in range(t):
    n = int(input())
    center = n//2
    for i in range(center, 0, -1):
        if arr[i] == 1 and arr[n-i] == 1:
            print(i, n-i)
            break

