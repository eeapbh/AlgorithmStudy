# 97~122
test = 'abcdefghijklmnopqrstuvwxyz'
line = input()

for i in range(len(test)):
    for j in range(len(line)):
        if test[i] == line[j]:
            print(j, end=' ')
            break
    else:
        print(-1, end=' ')
