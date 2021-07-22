import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
a = list(map(int, input()))
b = list(map(int, input()))

ans = 0
def switch(x, arr):

    for i in range(x-1, x+2):
        if 0<=i<n:
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0

while 1:
    if a == b:
        break
    if a[0] != b[0]:
        switch(0, b)
        ans += 1
        continue
    if a[n-1] != b[n-1]:
        switch(n-1, b)
        ans += 1
        continue

    for i in range(1, n-1):
        if a[i] != b[i]:
            switch(i, b)
            ans += 1
            break

print(ans)