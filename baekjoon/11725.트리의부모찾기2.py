from collections import deque
n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

ans = {}
q = deque()
q.append(1)
check = [0 for _ in range(n+1)]
while len(q)>0:
    parent = q.popleft()
    for i in tree[parent]:
        if not check[i]:
            ans[i] = parent
            q.append(i)
            check[i] = 1

for i in range(2, n+1):
    print(ans[i])

