n, k = map(int, input().split())
line = list(input())
ans = 0
for i in range(n):
    if line[i] == 'P':
        if i-k >=0:
            s = i-k
        else:
            s = 0
        if i + k <= n-1:
            e = i + k
        else:
            e = n - 1

        for j in range(s, e + 1):
            if line[j] == 'H':
                ans += 1
                line[j] = 'C'
                break
print(ans)
