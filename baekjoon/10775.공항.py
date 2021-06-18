import sys
sys.stdin = open('input.txt', 'r')
g = int(input())
p = int(input())
arr = [int(input()) for _ in range(p)]
gate = [0]*(g+1)
cnt = 0
for a in arr:
    for i in range(1, a+1):
        if gate[i] == 0:
            gate[i] = 1
            cnt += 1
            break
    else:
        break

print(cnt)