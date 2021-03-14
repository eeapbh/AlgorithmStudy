n = int(input())
cnt = 1
idx = 1
while cnt <= n:
     cnt += idx
     idx += 1
cnt -= idx
idx -= 1
while 1:
    for i in range(idx+1):
        cnt += 1
        if cnt == n:
            if idx % 2 == 1:
                print('{}/{}'.format(idx-i, i+1))
                break
            else:
                print('{}/{}'.format(i+1, idx-i))
                break
    if cnt == n:
        break
    idx += 1
# X = 14
# stage, key_X = 1, 1
# while key_X + stage <= X:
#     key_X += stage
#     stage += 1
# step = X - key_X
# x, y = step + 1, stage - step
# if stage % 2 == 0:
#     print('{}/{}'.format(x, y))
# else:
#     print('{}/{}'.format(y, x))