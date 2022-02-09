import sys
sys.setrecursionlimit(100000)
def postOrder(arr):
    n = len(arr)

    if n <= 1:
        return arr
    for i in range(1, n):
        if arr[i] > arr[0]:
            return postOrder(arr[1:i]) + postOrder(arr[i:]) + [arr[0]]
    return postOrder(arr[1:]) + [arr[0]]


arr = []
while 1:
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break

ans = postOrder(arr)
for i in ans:
    print(i)

