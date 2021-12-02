word = input()
st = 0

ans = 'YES'
while 1:
    if st >= len(word):
        break
    if word[st] == 'p':
        if len(word) - st < 2:
            ans = 'NO'
            break
        if word[st:st+2] == 'pi':
            st = st + 2
            continue
        else:
            ans = 'NO'
            break
    elif word[st] == 'k':
        if len(word) - st < 2:
            ans = 'NO'
            break
        if word[st:st+2] == 'ka':
            st = st + 2
            continue
        else:
            ans = 'NO'
            break
    elif word[st] == 'c':
        if len(word) - st < 3:
            ans = 'NO'
            break
        if word[st:st+3] == 'chu':
            st = st+3
            continue
        else:
            ans = 'NO'
            break
    else:
        ans = 'NO'
        break
print(ans)


