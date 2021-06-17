n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = 0
ans = 0
for a in arr:
    if s < a:
        s = a + l-1
        ans += 1
print(ans)
