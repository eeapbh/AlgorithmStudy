
def test(word):
    moum = 'aeiou'
    zaum = 'bcdfghjklmnpqrstvwxyz'
    test1 = 0
    test2 = 0
    test3 = 0

    for i in word:
        if i in moum:
            test1 = 1
            break
    if test1 == 0:
        return 0
    m = 0
    z = 0
    for i in word:
        if i in moum:
            m += 1
            z = 0
        if i in zaum:
            z += 1
            m = 0
        if m >= 3 or z >= 3:
            return 0

    tmp = word[0]
    for i in range(1, len(word)):
        if tmp == word[i]:
            if word[i] == 'e' or word[i] == 'o':
                continue
            else:
                return 0
        tmp = word[i]
    return 1




while 1:
    word = input()
    if word == 'end':
        break

    if test(word) == 0:
        print('<{}> is not acceptable.'.format(word))
    else:1
        print('<{}> is acceptable.'.format(word))
