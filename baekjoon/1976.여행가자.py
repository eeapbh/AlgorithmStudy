import sys
sys.setrecursionlimit(1000000)

n = int(input())
m = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

plan = list(map(int, input().split()))
for i in range(len(plan)):
    plan[i] -= 1


def dfs(s, e):
    if arr[s][e] == 1:
        return 1
    else:
        for i in range(n):
            if s != i and arr[s][i] == 1:
                dfs(i, e)
    return -1


for i in range(len(plan)-1):
    s, e = plan[i], plan[i+1]
    if dfs(s, e) == 1:
        continue
    else:
        print('NO')
        break
print('YES')

