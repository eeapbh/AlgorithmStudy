line = input()
tmp=[]
for i in line:
    if ord(i)>=65 and ord(i) <= 90:
        tmp += i

cnt = 0
for i in 'UCPC':

    for j in range(len(tmp)):
        if tmp[j] == i:
            tmp[j] = '0'
            cnt += 1
            break
        else:
            tmp[j] = '0'
    if cnt == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')


