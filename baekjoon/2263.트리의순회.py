import sys
sys.setrecursionlimit(1000000000)


n = int(sys.stdin.readline())
inOrder = list(map(int, sys.stdin.readline().split()))
postOrder = list(map(int, sys.stdin.readline().split()))

position = [0]*(n+1)
for i in range(n):
    position[inOrder[i]] = i
def preOrder(inst, ined, post, poed):
    if inst > ined or post > poed:
        return

    root = postOrder[poed]
    root_idx = position[root]
    print(root, end=' ')
    left = root_idx - inst
    right = ined - root_idx
    preOrder(inst, inst+left-1, post, post+left-1)
    preOrder(ined-right+1, ined, poed-right, poed-1)

preOrder(0, n-1, 0, n-1)
