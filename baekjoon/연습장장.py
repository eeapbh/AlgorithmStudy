a = 3
b = 5
c = 7
d = 1
from collections import deque
def solution(a,b,c,d):
    answer = -1
    q = deque()
    q.append((0, 0))
    check = [-1]*101
    if d > max(a, b, c):
        return -1
    while q:
        cx, cc = q.popleft()
        if cx == d:
            answer = cc
            break
        for i in (cx+a, cx-a, cx+b, cx-b, cx+c, cx-c):
            if 0<=i<=100 and check[i] == -1:
                q.append((i, cc + 1))
                check[i] = 1

    return answer

print(solution(a, b, c, d))
