n, m = map(int,(input().split()))
word1 = input()
word2 = input()
t = int(input())


word1 = word1[::-1]
word = word1+word2
word = list(word)
for _ in range(t):
    save = []
    for i in range(0, n+m-1):
        if word[i] in word1 and word[i+1] in word2:
            save.append(i)
            save.append(i+1)
    for s in range(0, len(save), 2):
        word[save[s]], word[save[s] + 1] = word[save[s] + 1], word[save[s]]


print(''.join(word))
