import re
n = int(input())
string = [input() for _ in range(n)]

for i in string:
    p = re.compile('(100+1+|01)+')
    rs = p.fullmatch(i)
    if rs:
        print('YES')
    else:
        print('NO')