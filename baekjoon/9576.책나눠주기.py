t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = [0]*(n+1)
    cnt = 0
    save = []
    for i in range(m):
        tmp = list(map(int, input().split()))
        save.append(tmp)
    save.sort(key=lambda x:x[1])
    for s in save:

        for j in range(s[0], s[-1] + 1):
            if arr[j] == 0:
                arr[j] = 1
                cnt += 1
                break

    print(cnt)


