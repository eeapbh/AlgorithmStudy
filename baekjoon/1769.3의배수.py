a = input()
ans = 0
rs = 'NO'
tmp = 0
while 1:

    if int(a) <= 9:
        tmp = int(a)
        break

    ans += 1
    tmp = 0
    for i in a:
        tmp += int(i)
    if tmp <= 9:

        break
    a = str(tmp)

if tmp == 3 or tmp == 6 or tmp == 9:
    print(ans)
    print('YES')
else:
    print(ans)
    print('NO')
