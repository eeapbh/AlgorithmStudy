n = int(input())
tree = [[] for _ in range(n)]
arr = list(map(int, input().split()))
m = int(input())
root = -1
cnt = 0

def dfs(node):
    global cnt
    if not tree[node]:
        cnt += 1
        return
    for j in range(len(tree[node])):
        if tree[node][j] == m:
            if len(tree[node]) == 1:
                cnt += 1
            else:
                continue
        else:
            dfs(tree[node][j])

for i in range(n):
    if arr[i] == -1:
        root = i
    else:
        tree[arr[i]].append(i)

if m == root:
    print(0)
else:
    dfs(root)
    print(cnt)