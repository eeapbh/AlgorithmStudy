
def dfs(cur, prev, tree, check):
    check[cur] = 1
    for i in tree[cur]:
        if i == prev:
            continue
        if check[i]:
            return 0
        if not dfs(i, cur, tree, check):
            return 0
    return 1



def count_tree(n, tree, check):
    cnt = 0
    for i in range(1, n+1):
        if not check[i] and dfs(i, 0, tree, check):
            cnt += 1
    return cnt

trg = 0
res = []
while 1:
    trg += 1
    s, e = map(int, input().split())
    if s == 0 and e == 0:
        break


    tree = [[] for _ in range(s+1)]
    for i in range(e):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    check = [0 for _ in range(s + 1)]
    cnt = count_tree(s, tree, check)
    if cnt == 0:
        res.append("Case %d: No trees." % trg)
    elif cnt == 1:
        res.append("Case %d: There is one tree." % trg)
    else:
        res.append("Case %d: A forest of %d trees." % (trg, cnt))

for a in res:
    print(a)





