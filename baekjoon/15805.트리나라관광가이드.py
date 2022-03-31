n = int(input())
arr = list(map(int, input().split()))
root = arr[0]
k = max(arr)
visit = [0]*(k + 1)

ans = [0]*(k + 1)
p = 0
for a in arr:
    if visit[a] == 0:
        visit[a] = 1
        ans[a] = p
        p = a

    elif visit[a] == 1:

        p = a
ans[root] = -1
print(k + 1)
print(*ans)

