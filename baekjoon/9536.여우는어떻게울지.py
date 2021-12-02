t = int(input())
for _ in range(t):
    line = list(input().split())
    tmp = []
    while 1:
        info = list(input().split())
        if info[-1] == 'say?':
            break

        tmp.append(info[-1])

    for i in line:
        if not i in tmp:
            print(i, end=' ')
    print()