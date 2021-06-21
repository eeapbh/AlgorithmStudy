import sys
sys.stdin = open('input.txt', 'r')
g = int(input())
p = int(input())
arr = [int(input()) for _ in range(p)]
gate = [i for i in range(g + 1)]

def union(x, y):

    a = find(x)
    b = find(y)
    gate[a] = b


def find(x):
    if gate[x] == x:
        return x
    gate[x] = find(gate[x])
    return gate[x]

cnt = 0
for i in arr:
    p = find(i)
    if p == 0:
        break
    else:
        union(p, p-1)
        cnt += 1

print(cnt)
