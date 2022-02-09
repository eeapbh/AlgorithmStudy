from itertools import combinations
k = 3
d = 4
prices = [4, 5, 6, 7, 8, 9]
arr = list(combinations(prices, k))
print(arr)
rs = []
for a in arr:
    if a[-1] - a[0] <=d:
       rs.append(sum(a)//len(a))
ans = min(rs)
print(ans)
print(prices[(len(prices)//2)-1])