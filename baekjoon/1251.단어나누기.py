from itertools import product

word = input()
arr = [i for i in range(1, len(word) - 1)]
# print(arr)
per = list(product(arr, arr, arr))
save = []
for p in per:
    if sum(p) == len(word):
        save.append(p)

# print(save)
save2 = []
for s in save:
    a = s[0]
    b = s[1]

    w1 = word[0:a]
    w2 = word[a:a + b]
    w3 = word[a + b:]
    tmp = w1[::-1] + w2[::-1] + w3[::-1]
    save2.append(tmp)

    # print(w1, w2, w3)
# print(save2)
save2.sort()
print(save2[0])