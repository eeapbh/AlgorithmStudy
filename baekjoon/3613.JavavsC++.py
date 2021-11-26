word = input()
ans = ''
trg = 0
err = 0
if '_' in word:# c++일때
    for i in word:
        if 65 <= ord(i) <= 90:# c++에서 대문자가 나올때
            err = 1
            break
        if i != '_':
            if trg == 1:
                ans += chr(ord(i) - 32)
                trg = 0
            else:
                ans += i
        else:
            if len(ans) == 0:
                err = 1
                break
            if word.index(i) == len(word) - 1:
                err = 1
                break

            if trg == 1:
                err = 1
                break
            else:
                trg = 1
else:
    for i in range(len(word)):
        if 65 <= ord(word[i]) <= 90:
            if i == 0:
                # ans += chr(ord(word[i]) + 32)
                err = 1
                break
            else:
                ans += '_' + chr(ord(word[i]) + 32)
        else:
            ans += word[i]
if err == 1:
    print('Error!')
else:
    print(ans)
