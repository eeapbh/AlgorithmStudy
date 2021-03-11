import sys
sys.stdin = open('input.txt', 'r')
arr = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
n = len(word)
count = 0
save = []
for i in range(n):
    if word[i:i+3] == 'dz=':
        save.append(i)

for i in range(len(save)):
    word = word[0:save[i]] +'111' + word[save[i]+3:n]

for i in range(n):
    if word[i:i+2] in arr:
        count += 1

print(len(save) + len(word) - count - word.count('1'))
