import sys
sys.stdin = open('input.txt', 'r')
info = input()
word = input()
s = 0
n = len(word)
ans = 0
while 1:
    if s > len(info)-n:
        break
    a = info[s:s+n]
    if a == word:
        s = s+n
        ans += 1
    else:
        s = s+1
print(ans)