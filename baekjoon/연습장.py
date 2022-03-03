save = []
for i in range(1, 10000):
    num = i
    tmp = str(i)
    for t in tmp:
        num += int(t)
    save.append(num)

for j in range(1, 10000):
    if j not in save:
        print(j)


