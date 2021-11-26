t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    tmp1 = ('WB'*50000)[:n]
    tmp2 = ('BW'*50000)[:n]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    for i in range(n):
        if a[i] != tmp1[i]:
            cnt1 += 1
        if a[i] != tmp2[i]:
            cnt2 += 1
    for i in range(n):
        if b[i] != tmp1[i]:
            cnt3 += 1
        if b[i] != tmp2[i]:
            cnt4 += 1

    if cnt1 % 2 == 0:
        if abs(a.count('W') - b.count('B')) == 1:
            cnt1 = cnt1//2
    if cnt2 % 2 == 0:
        if abs(a.count('W') - b.count('B')) == 1:
            cnt2 = cnt2 // 2
    if cnt3 % 2 == 0:
        if abs(a.count('W') - b.count('B')) == 1:
            cnt3 = cnt3 // 2
    if cnt4 % 2 == 0:
        if abs(a.count('W') - b.count('B')) == 1:
            cnt4 = cnt4 // 2

    ans = min(cnt1, cnt2) + min(cnt3, cnt4)
    print(ans)