tc = 0
while 1:
    tc += 1
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    ans = (v // p) * l

    if v % p <= l:
        ans += v % p
    else:
        ans += l
    print('Case {}: {}'.format(tc, ans))

