n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().split()))
rs = []
for a in arr:
    cnt = 1
    for b in arr:
        if a[0] < b[0] and a[1] < b[1]:
            cnt += 1
    print(cnt, end=' ')
