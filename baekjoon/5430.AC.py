from collections import deque
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline()
    if n != 0:
        arr = arr[1:-2]
        arr = deque(arr.split(','))
    else:
        arr = []
    trg = True

    for i in p:
        # if n == 0:
        #     print('error')
        #     break
        if i == 'R':
            trg = not trg
        elif i == 'D':
            if arr:
                if trg:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print('error')
                break
    else:
        if not trg:
            arr.reverse()

        ans = '[' + ",".join(arr) + ']'
        print(ans)
