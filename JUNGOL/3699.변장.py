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

    for v in dic.values():
        ans *= (len(v)+1)
    print(ans-1)