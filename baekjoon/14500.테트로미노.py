import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


d = [[(0, 1), (0, 2), (0, 3)],
     [(1, 0), (2, 0), (3, 0)],

     [(0, 1), (1, 0), (1, 1)],

     [(1, 0), (2, 0), (2, 1)],
     [(1, 0), (2, 0), (2, -1)],
     [(0, 1), (1, 0), (2, 0)],
     [(0, 1), (1, 1), (2, 1)],
     [(0, 1), (0, 2), (-1, 2)],
     [(1, 0), (1, 1), (1, 2)],

     [(1, 0), (1, 1), (2, 1)],
     [(1, 0), (1, -1), (2, -1)],
     [(-1, 0), (-1, 1), (-2, 1)],
     [(-1, 0), (-1, -1), (-2, -1)],
     [(0, 1), (-1, 1), (-1, 2)],
     [(0, 1), (1, 1), (1, 2)],

     [(0, 1), (0, 2), (1, 1)],
     [(0, 1), (0, 2), (-1, 1)],
     [(1, 0), (2, 0), (1, -1)],
     [(1, 0), (2, 0), (1, 1)]]
ans = []
def check(x, y):
    for i in d:
        tmp = arr[x][y]
        for j in range(3):
            nx = x + i[j][0]
            ny = y + i[j][1]
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
               break
            else:
                tmp += arr[nx][ny]
                if j == 2:
                    ans.append(tmp)

for i in range(n):
    for j in range(m):
        check(i, j)

print(max(ans))
