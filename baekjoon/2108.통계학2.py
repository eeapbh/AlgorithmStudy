import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]


print(round(sum(arr)/n))
arr2 = arr[::]
arr2.sort()
print(arr2[n//2])
check = [0]*8001
for i in arr:
    check[i+4000] += 1
M = max(check)
tmp = []
for i in range(8001):
    if check[i] == M:
        tmp.append(i)
if len(tmp) == 1:
    print(tmp[0] - 4000)
else:
    print(tmp[1] - 4000)
print(arr2[-1] - arr2[0])