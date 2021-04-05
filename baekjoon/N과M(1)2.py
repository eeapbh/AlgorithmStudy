from itertools import permutations
n, m = map(int, input().split())
arr = [a for a in range(1, n+1)]
rs = list(permutations(arr, m))
for r in rs:
    print(*r)