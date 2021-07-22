n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for a in arr:
    if a <= l:
        l += 1
print(l)
