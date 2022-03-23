dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
trueD = [(0, 1), (1, 0), (0, -1), (-1, 0)]
falseD = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = 5
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
    while cnt < n*n:


        for i in range(4):
            tmp = num
            ans[x][y] = tmp
            for j in range(n-1):
                tmp += 1
                nx = x + d[i%4][0]
                ny = y + d[i%4][1]
                if 0<=nx<n-d[i%4][0] and 0<=ny<n-d[i%4][1]:
                    ans[nx][ny] = tmp
                    cnt += 1
                    x = nx
                    y = ny
                else:
                    x = nx
                    y = ny


        print(tmp)
        num = tmp
        n = n-1



    return ans


print(solution(n, clockwise))