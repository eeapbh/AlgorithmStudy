word = input()
n = len(word)
for i in range(n):
    if word[i:] == word[i:][::-1]:
        print(n+i)
        break
