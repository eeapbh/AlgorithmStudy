n = int(input())
ans = 0
for i in range(n):
    word = input()
    for w in word:
        long = word.count(w)
        if w*long not in word:
            break
    else:
        ans += 1
print(ans)

# https://aisiunme.github.io/algorithm/2018/08/13/baekjoon-group-word-checker-1316.md/