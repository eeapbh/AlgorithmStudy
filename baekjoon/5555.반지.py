pattern = input()
n = int(input())
ans = 0
for _ in range(n):
    line = input()
    tmp = line + line
    if pattern in tmp:
        ans += 1
print(ans)