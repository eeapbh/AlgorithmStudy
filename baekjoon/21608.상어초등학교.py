n = int(input())
arr = [[0]*n for _ in range(n)]

info = {}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, like):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] in like:
                cnt += 1
    return cnt

def dfs2(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if arr[nx][ny] == 0:
                cnt += 1
    return cnt

def dfs3(x, y, li):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] in li:
                cnt += 1
    if cnt == 0:
        return 0
    else:
        return 10**(cnt-1)


def check1(num, like):
    big = -1
    c = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                rs = dfs(i, j, like)
                visit[i][j] = rs
                if rs > big:
                    big = rs
    for i in range(n):
        for j in range(n):
            if visit[i][j] == big:
                c.append((i, j))

    return c

def check2(li):
    big = -1
    check2tmp = []
    for i in li[::-1]:
        a = dfs2(i[0], i[1])
        if a >= big:
            big = a
            check2tmp.append((i[0], i[1]))
    # print("check2tmp", check2tmp)
    return (check2tmp[-1][0], check2tmp[-1][1])

def last():
    ans = 0
    for i in range(n):
        for j in range(n):
            ans += dfs3(i, j, info[arr[i][j]])
    return ans


for i in range(n*n):
    tmp = list(map(int, input().split()))
    info[tmp[0]] = tmp[1:]

# print(info)
trg = 0


for k, v in info.items():
    visit = [[0]*n for _ in range(n)]
    if trg == 0:
        if n % 2 == 1:
            arr[n//2][n//2] = k
            trg += 1
            continue
        else:
            arr[(n-1)//2][(n-1)//2] = k
            trg += 1
            continue
    else:
        check1rs = check1(k, v)
        # print("check1rs", check1rs)
        if len(check1rs) == 1:
            arr[check1rs[0][0]][check1rs[0][1]] = k
        elif len(check1rs) > 1:
            x, y = check2(check1rs)
            arr[x][y] = k
# print(arr)
print(last())

