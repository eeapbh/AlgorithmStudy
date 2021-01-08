n = int(input())

arr = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            arr[i][j] += 1


ans = 0
for i in range(100):
    ans += sum(arr[i])

print(ans)