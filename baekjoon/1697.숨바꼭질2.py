from collections import deque
n, k = map(int, input().split())
q = deque()
q.append((n, 0))
cnt = 0
memo = [-1]*100001
while q:
    cx, cc = q.popleft()
    if cx == k:
        break
    for i in (cx+1, cx-1, 2*cx):
        if 0<=i<=100000 and memo[i] == -1:
            q.append((i, cc + 1))
            memo[i] = 1

print(cc)