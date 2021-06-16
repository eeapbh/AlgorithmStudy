n, m = map(int, input().split())
arr1 = [list(input()) for _ in range(n)]
arr2 = [list(input()) for _ in range(n)]

def change(i, j):
    if i > n-3:
        a = n- 3
    else:
        a = i

    if j > m-3:
        b = m-3
    else:
        b = j
    for x in range(a, a + 3):
        for y in range(b, b + 3):
            if arr1[x][y] == '1':
                arr1[x][y] = '0'
            else:
                arr1[x][y] = '1'
    # print(arr1, arr2)

def check():
    cnt = 0
    if n < 3 or m < 3:
        if arr1 == arr2:
            return 0
        else:
            return -1
    for i in range(n):
        for j in range(m):
            if arr1[i][j] != arr2[i][j]:
                change(i, j)
                cnt += 1
                if arr1 == arr2:
                    return cnt
    return -1
print(check())