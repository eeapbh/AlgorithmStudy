arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
    'eight', 'nine', 'ten']
m, n = map(int, input().split())
rs = []
rs2 = []
for i in range(m, n + 1):
    i = str(i)
    tmp = ''
    for j in i:

        tmp += arr[int(j)]
        tmp += ' '
    rs.append(tmp)
rs.sort()

for r in rs:
    tmp = ''
    a = list(r.split())

    for b in a:
        tmp += str(arr.index(b))

    rs2.append(int(tmp))

cnt = 0
for r in rs2:

    if cnt == 10:
        cnt = 0
        print()
    print(r, end=' ')
    cnt += 1