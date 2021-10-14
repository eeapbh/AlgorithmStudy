import sys
t = int(input())
def check():
    arr.sort()
    for i in range(n - 1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            print('NO')
            return
    print('YES')



for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    check()
