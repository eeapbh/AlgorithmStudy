n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
arr2 = list(zip(*arr))
ans = ''
for i in arr2:
    tmp = list(sorted(i))
    M_cnt = -1
    M = ''
    for j in range(n-1, -1, -1):
        if tmp.count(tmp[j]) >= M_cnt:
            M_cnt = tmp.count(tmp[j])
            M = tmp[j]


    ans += M
ans2 = 0
for i in arr:
    for j in range(m):
        if i[j] != ans[j]:
            ans2 += 1
print(ans)
print(ans2)


