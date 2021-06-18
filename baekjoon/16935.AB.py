import sys
sys.stdin = open('input.txt', 'r')

a, b = map(int, input().split())
b = str(b)
cnt = 1
while 1:
    if a == int(b):
        print(cnt)
        break
    if a > int(b):
        print(-1)
        break
    if int(b) % 2 == 0:
        b = int(b) // 2
        b = str(b)
        cnt += 1
    elif b[-1] == '1':
        b = b[:-1]
        cnt += 1
    else:
        print(-1)
        break
