n = int(input())
save = []
for _ in range(n):
    word = input()
    tmp = ''

    for i in word:
        if 97 <= ord(i) <= 122:
            if tmp != '':
                save.append(tmp)
            tmp = ''
            continue
        else:
            tmp += i
    if tmp != '':
        save.append(tmp)
# print(save)
save2 = list(map(int, save))
save2.sort()
for i in save2:
    print(i)