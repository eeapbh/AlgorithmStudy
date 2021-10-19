line = input()
n = len(line)
word = ''
ans = ''
trg = 0
for i in range(n):
    if trg == 0:
        if line[i] == '<':
            trg = 1
            word += line[i]
        elif line[i] == ' ':
            word += line[i]
            ans += word
            word = ''
        else:
            word = line[i] + word
    else:
        word += line[i]
        if line[i] == '>':
            trg = 0
            ans += word
            word = ''
print(ans + word)

