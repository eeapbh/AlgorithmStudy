import sys
sys.stdin = open('input.txt', 'r')
t = int(input())
for tc in range(t):
    h, w, n = map(int, input().split())

    cnt = 0
    for i in range(w):
        for j in range(h):
            cnt += 1
            if cnt == n:
                if i +1 < 10:
                    # print('{}0{}'.format(j+1, i+1))
                    print(j+1, end='')
                    print(0, end='')
                    print(i+1)
                else:
                    # print('{}{}'.format(j + 1, i + 1))
                    print(j + 1, end='')
                    print(i + 1)