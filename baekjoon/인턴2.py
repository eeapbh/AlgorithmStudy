sentence = "encrypt this sentence"
sentence = list(sentence)
keyword = "something"
skips = [0, 1, 3, 2, 9, 2, 0, 3, 0, 2, 4, 1, 3]
st = 0
d = -1
n = len(sentence)


for s in skips:
    if st > n + d+1:
        break
    d += 1
    k = d % len(keyword)
    if st +s > n + d:
        break
    for i in range(st, st + s):
        if keyword[k] == sentence[i]:
            sentence.insert(i+1, keyword[k])
            st = i+2
            break

    else:
        sentence.insert(st + s, keyword[k])
        st += s+1

print(''.join(sentence))



