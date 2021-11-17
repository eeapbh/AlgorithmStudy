import sys
sys.stdin = open('input.txt')
import time
start = time.time()
arr = list(map(int, input().split(',')))
a = []
b = []

for i in arr:
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)
A = 0
B = 0
if len(a) == 0:
    A = 0
else:
    A = max(a)

if len(b) == 0:
    B = 0
else:
    B = max(b)
print(A + B)
print('연습장장', time.time() - start)