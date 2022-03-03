import sys
sys.setrecursionlimit(1000000)
def dfs(x):
    global ans
    visit[x] = 1
    tmp.append(x)
    num = arr[x]
    if visit[num] == 1:
        if num in tmp:
            ans += tmp[tmp.index(num):]
        return
    else:
        dfs(num)



t = int(input())
for _ in range(t):
    n = int(input())
    arr =[0] + list(map(int, input().split()))
    visit = [0]*(n + 1)
    ans = []
    for i in range(1, n+1):
        if visit[i] == 0:
            tmp = []
            dfs(i)

    print(n - len(ans))