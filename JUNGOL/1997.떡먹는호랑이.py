d, k = map(int, input().split())
arr = [0]*31
def f(x):
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2
    for i in range(3, x+1):
        arr[i] = arr[i-2] + arr[i-1]
    return arr[x]

def check():
    for i in range(1,10000):
        for j in range(1, i):
            if f(d - 3) * j + f(d - 2) * i == k:
                return j, i

a, b = check()
print(a)
print(b)

