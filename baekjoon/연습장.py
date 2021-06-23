import sys
sys.stdin = open('input.txt', 'r')

g = int(input())
p = int(input())
arr = [int(input()) for _ in range(p)]
gate = [i for i in range(g+1)]
def union(x, y):
    a = find(x)
    b = find(y)
    gate[a] = b

def find(x):
    if x == gate[x]:
        return x
    else:
        gate[x] = find(gate[x])
        return (gate[x])


cnt = 0
for i in arr:
    a = find(i)
    if a != 0:
        union(a, a-1)
        cnt += 1
    else:
        break
print(cnt)