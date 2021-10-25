import sys
# sys.stdin = open('input.txt', 'r')
dic = {}
n = 0
while 1:
    a = sys.stdin.readline().rstrip()
    if not a:
        break

    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
    n += 1

name = list(dic.keys())
name.sort()

for k in name:
    print('%s %.4f' %(k, dic[k]*100/n))

