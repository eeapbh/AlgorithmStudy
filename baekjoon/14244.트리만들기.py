n, m = map(int, input().split())
save = 0
if m == 2:
    for i in range(n - 1):
        print(i, i + 1)
else:
    for i in range(1, n):
        if save < m:
            print(0, i)
            save += 1
        else:
            for j in range(save, n-1):
                print(j, j + 1)
