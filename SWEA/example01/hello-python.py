import sys
sys.stdin = open('a.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    elist = []
    plist = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                plist.append((i, j))
            elif arr[i][j] == 2:
                elist.append((i, j))

    road = []
    for e in elist:
        tmp = []
        for p in plist:
            tmp.append(abs(p[0]-e[0]) + abs(p[1]-e[1]))
        road.append(tmp)

    time = 1
    while 1:
        temp = 0
        for i in range(len(elist)):
            temp += sum(road[i])
        if temp == 100 * len(elist) * len(plist):
            rs = time
            break
        for i in range(len(elist)):
            for j in range(len(plist)):
                if road[i][j] <= time:
                    for k in range(len(elist)):
                        road[k][j] = 100
                    break
        time += 1
    print('#{} {}'.format(tc, time))