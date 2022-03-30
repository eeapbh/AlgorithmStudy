import sys
sys.stdin = open('input.txt','r')

k = int(input())
tree = list(map(int, input().split()))
save = [[] for _ in range(k)]

def inOrder(tree, depth):
    n = len(tree)
    if n == 1:
        save[depth].append(tree[0])
        return
    mid = n//2
    save[depth].append(tree[mid])
    inOrder(tree[:mid], depth + 1)
    inOrder(tree[mid+1:], depth + 1)


inOrder(tree, 0)
for s in save:
    print(*s)