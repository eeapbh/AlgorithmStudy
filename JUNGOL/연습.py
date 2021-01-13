arr = [0]*31

def f(x):
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2
    for i in range(3, x+1):
        arr[i] = arr[i-2] + arr[i-1]
    return arr[x]



print(f(5))