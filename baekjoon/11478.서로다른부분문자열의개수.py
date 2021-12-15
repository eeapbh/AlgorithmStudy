word = (input())

save = set()
for i in range(len(word)):
    for j in range(i, len(word)):
        save.add(word[i:j+1])
print(len(save))
