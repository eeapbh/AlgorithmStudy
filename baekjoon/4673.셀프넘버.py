def check(num):
    tmp = num
    num = str(num)
    for i in num:
        tmp += int(i)
    save.append(tmp)
save = []
for i in range(10000):
    check(i)

for i in range(10000):
    if i not in save:
        print(i)

