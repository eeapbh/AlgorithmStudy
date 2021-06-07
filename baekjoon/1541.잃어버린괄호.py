info = input().split('-')
# print(info)
tmp = 0
for i in info[0].split('+'):
    tmp += int(i)
ans = tmp
for i in range(1, len(info)):
    tmp = 0
    for j in info[i].split('+'):
        tmp += int(j)
    ans -= tmp
print(ans)