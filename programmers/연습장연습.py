from copy import deepcopy
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
trueD = [(0, 1), (1, 0), (0, -1), (-1, 0)]
falseD = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = 6
clockwise = True
def solution(n, clockwise):
    ans = [[0]*n for _ in range(n)]
    d = []
    if clockwise == True:
        d = trueD
    else:
        d = falseD
    cnt = 0
    x, y = 0, 0

    ans[0][0] = 1
    num = 1

    if n % 2 == 0:
        end = n*n //4
    else:
        end = (n*n //4) + 1
    s = 0
    while 1:
        x = s
        y = s
        for i in range(4):
            trg = 0
            tmp = num
            if tmp == end:
                print('여기1')
                arr2 = deepcopy(ans)
                for i in range(n):
                    for j in range(n):
                        if arr2[i][j] == 0:
                            arr2[i][j] = end

                arr2 = deepcopy(ans)
                print(ans)
                print(arr2)
                return arr2
            ans[x][y] = tmp
            for j in range(n-1):
                if tmp == end:
                    print('여기1')
                    for i in range(n):
                        for j in range(n):
                            if ans[i][j] == 0:
                                ans[i][j] = end

                    arr2 = deepcopy(ans)
                    return ans
                tmp += 1
                nx = x + d[i%4][0]
                ny = y + d[i%4][1]
                if trg < n - 2:
                    ans[nx][ny] = tmp
                    cnt += 1
                    x = nx
                    y = ny
                    trg += 1
                else:
                    x = nx
                    y = ny
        s += 1
        print(tmp)
        num = tmp
        n = n-2

    return ans


ans = (solution(n, clockwise))
for i in ans:
    print(i)