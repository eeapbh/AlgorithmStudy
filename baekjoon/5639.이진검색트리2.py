import sys
sys.setrecursionlimit(100000)

def postOrder(st, ed):
    if st > ed:
        return
    root = arr[st]
    idx = st + 1
    while idx <= ed:
        if arr[idx] > root:
            break
        idx += 1
    postOrder(st + 1, idx -1)
    postOrder(idx, ed)
    print(root)



arr = []
while 1:
    try:
        arr.append(int(sys.stdin.readline()))
    except:
        break

postOrder(0, len(arr) - 1)

