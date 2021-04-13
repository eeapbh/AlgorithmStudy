arr = [list(map(int, input().split())) for _ in range(9)]
arr2 = []
def garo(li):
    x = 45 - sum(li)
    li[li.index(0)] = x

def sero(li):
    x = 45 - sum(li)
    li[li.index(0)] = x

for i in range(9):
    tmp = arr[i:i+1]
    if tmp.count(0) == 1:
        garo(tmp)
        arr2.append(tmp)
    else:
        arr2.append(tmp)
for i in range(9):
    tmp = []
    for j in range(9):
        tmp.append(arr[j][i])
        if arr[j][i] == 0:
            check = (j, i)
    if tmp.count(0) == 1:
        x = 45 - sum(tmp)
        arr[j][i] = x

for i in range(0, 7, 3):
    for j in range(0, 7, 3):

