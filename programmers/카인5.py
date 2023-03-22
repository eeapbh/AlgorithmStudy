rc =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operations =["Rotate", "ShiftRow"]
from copy import deepcopy

def solution(rc, operations):

    answer = [[]]
    n = len(rc)
    m = len(rc[0])
    for o in operations:
        if o == 'ShiftRow':
            a = rc.pop(0)
            rc.append(a)
        else:
            tmp = deepcopy(rc)
            a = rc[0][0:m-1]
            ziparr = list(zip(*rc))
            b = ziparr[-1][0:n-1]
            c = rc[-1][1:]
            d = ziparr[0][1:]
            print(a, b, c, d)
            print(ziparr)
            for i in range(1, m):
                tmp[0][t] = a[t-1]
            for



    return answer

print(solution(rc, operations))