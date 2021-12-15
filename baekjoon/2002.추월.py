n = int(input())
arr1 = list(input() for _ in range(n))
arr2 = list(input() for _ in range(n))

tmp = []
for i in arr2:
    if i in arr1:
        tmp.append(arr1.index(i))
ans = 0

rs = 0
for i in range(n):
    for j in range(i, n):
        if tmp[i] > tmp[j]:
            ans += 1
            break
print(ans)