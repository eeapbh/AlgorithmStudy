import sys
sys.stdin = open('b.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    rs = []
    home = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                home.append((i, j))


    tmp = []
    # 가로
    for i in range(h):
        if sum(arr[i]) == 0:
            tmp = []
            for ho in home:
                tmp.append(abs(ho[0]-i))
            rs.append(max(tmp))
    print(rs)

    #세로
    for a in range(w):
        tmp = []
        tmp2 = 0
        for b in range(h):
            tmp2 += arr[b][a]
        if tmp2 == 0:
            for ho in home:
                tmp.append(abs(ho[1]-a))
            rs.append(max(tmp))
    print(rs)

    # 대각 /이 방향

    for i in range(1, h):
        tmp = []
        tmp3 = 0
        hab = i
        for j in range(i, -1, -1):
        #     print(j,hab-j, end=" ")
        # print()
            if hab-j < w and j < h:
                tmp3 += arr[j][hab-j]
            if tmp3 == 0:
                for ho in home:
                    tmp.append(abs(ho[0]-j-ho[1]))
                rs.append(max(tmp))
    print(rs)

    for i in range(1, h):
        hab = h-1+i
        tmp = []
        tmp4 = 0
        for j in range(i, w):
        #     print(hab-j, j, end=" ")
        # print()
            if hab-j < h and j < w:
                tmp4 += arr[hab-j][j]
            if tmp4 == 0:
                for ho in home:
                    tmp.append(abs(hab-ho[1])- ho[0])
                rs.append(max(tmp))
    # print(rs)

    # 대각 반대방향
    for i in range(w-1):
        minus = w-1-1-i
        tmp =[]
        tmp5 = 0
        for j in range(i+2):
            if j < h and j+minus < w:
    #     #         print(j,j+minus, end=" ")
    #     # print()
                tmp5 += arr[j][j+minus]
            if tmp5 == 0:
                for ho in home:
                    tmp.append(abs(ho[0]+minus-ho[1]))
                rs.append(max(tmp))
    # print(rs)
    for i in range(1, h-1):
        tmp = []
        tmp6 = 0
        minus = i
        for j in range(0, h-1):
            if j+i <h and j < w:
    #     #         print(j+i,j, end=" ")
    #     # print()
                tmp6 += arr[j+i][j]
            if tmp6 == 0:
                for ho in home:
                    tmp.append(abs(ho[1]+i)- ho[0])
                rs.append(max(tmp))
    print(rs)
    if len(rs) == 0:
        print('#{} {}'.format(tc, -1))
    else:
        print('#{} {}'.format(tc, min(rs)))




