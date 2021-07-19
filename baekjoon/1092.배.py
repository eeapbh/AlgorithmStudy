import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
crain = list(map(int, input().split()))
crain.sort(reverse=True)
m = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)
tmp = []
cnt = 0
if box[0] > crain[0]:
    print(-1)

else:
    while len(box):
        cnt += 1
        for i in crain:
            for j in box:
                if i >= j:
                    box.remove(j)
                    break
    print(cnt)