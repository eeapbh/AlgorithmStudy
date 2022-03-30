from collections import deque

n, k = map(int, input().split())

visit = [0]*100001
memo = [0]*100001
q = deque()
q.append((n, 0))
visit[n] = 1
while q:
    x, c = q.popleft()

    if x == k:
        e = k
        ans = []
        while 1:
            if e == n:
                ans.append(e)
                break
            ans.append(e)
            e = memo[e]
        print(c)
        print(*ans[::-1])
        break
    for i in (x - 1, x + 1, 2*x):
        if visit[i] == 0 and 0<=i<100001:
            visit[i] = 1
            memo[i] = x
            q.append((i, c + 1))



