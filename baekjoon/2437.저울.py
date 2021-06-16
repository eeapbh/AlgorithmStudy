n = int(input())
arr = list(map(int, input().split()))
arr.sort()

t = 1
for a in arr:
    if t < a:
        break
    t += a

print(t)