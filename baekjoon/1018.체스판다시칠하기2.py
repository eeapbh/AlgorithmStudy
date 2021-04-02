import sys
sys.stdin = open('input.txt')
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
chess1 = [['W', 'B','W', 'B','W', 'B','W', 'B'],['B','W', 'B','W', 'B','W', 'B','W'],
          ['W', 'B','W', 'B','W', 'B','W', 'B'],['B','W', 'B','W', 'B','W', 'B','W'],
          ['W', 'B','W', 'B','W', 'B','W', 'B'],['B','W', 'B','W', 'B','W', 'B','W'],
          ['W', 'B','W', 'B','W', 'B','W', 'B'],['B','W', 'B','W', 'B','W', 'B','W'],]

chess2 = [['B','W', 'B','W', 'B','W', 'B','W'],
          ['W', 'B','W', 'B','W', 'B','W', 'B'],['B','W', 'B','W', 'B','W', 'B','W'],
          ['W', 'B','W', 'B','W', 'B','W', 'B'],['B','W', 'B','W', 'B','W', 'B','W'],
          ['W', 'B','W', 'B','W', 'B','W', 'B'],['B','W', 'B','W', 'B','W', 'B','W'],
          ['W', 'B','W', 'B','W', 'B','W', 'B']]

rs = []
for i in range(n-8+1):
    for j in range(m-8+1):
        cnt1 = 0
        cnt2 = 0
        for x in range(i, i+8):
            w = b = 0
            for y in range(j, j+8):
                if arr[x][y] != chess1[x-i][y-j]:
                    cnt1 += 1
                elif arr[x][y] != chess2[x-i][y-j]:
                    cnt2 += 1
        rs.append(min(cnt1, cnt2))

print(min(rs))
