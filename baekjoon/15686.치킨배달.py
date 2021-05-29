import sys
sys.stdin = open('input.txt', 'r')
from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

rs = []
CombiChicken = list(combinations(chicken, m))
# print(chicken)

for c in CombiChicken:
    tmp1 = 0
    for h in home:
        tmp2 = []
        for i in c:
            tmp2.append(abs(h[0] - i[0]) + abs(h[1] - i[1]))
        tmp1 += (min(tmp2))
    rs.append(tmp1)
# print(rs)
print(min(rs))