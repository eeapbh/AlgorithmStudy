import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    dic = {}
    for i in range(n):
        a, b = input().split()
        if b in dic.keys():
            dic[b].append(a)
        else:
            dic[b] = [a]
    ans = 1
    ans2 = 0
    for v in dic.values():
        ans *= len(v)
        ans2 += len(v)
    if len(dic) == 1:
        print(ans)
    else:
        print(ans + ans2)