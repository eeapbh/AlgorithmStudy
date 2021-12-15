t = int(input())


for _ in range(t):
    arr = [0] * 91
    word = input()
    ans = 'OK'
    trg = 0
    for i in range(len(word)):
        if trg == 0:
            arr[ord(word[i])] += 1
        else:
            trg = 0
            continue
        if arr[ord(word[i])] % 3 == 0:
            if i == len(word) - 1 or word[i+1] != word[i]:
                ans = 'FAKE'
            else:
                trg = 1

    print(ans)


