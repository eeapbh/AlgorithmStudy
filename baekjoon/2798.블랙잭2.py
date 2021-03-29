from itertools import combinations
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(combinations(arr, 3))
Min = 123456789
for a in arr2:
    if sum(a) <= m and m - sum(a) < Min:
        Min = m-sum(a)
        ans = sum(a)
print(ans)
