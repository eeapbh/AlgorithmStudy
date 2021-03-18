n = int(input())
numbers = list(map(int, input().split()))
ans = 0
for i in numbers:
    if i == 1:
        continue
    else:
        cnt = 0
        for j in range(1, 1 + int((i ** (1/2)))):
            if i % j == 0:
                cnt += 1
        if cnt == 1:
            ans += 1
print(ans)
