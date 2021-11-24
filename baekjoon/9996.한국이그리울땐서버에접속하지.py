n = int(input())
s, e = input().split('*')
for i in range(n):
    word = input()

    if len(word) < len(s) + len(e):
        print('NE')
    elif s == word[0:len(s)] and e == word[-len(e):]:
        print('DA')
    else:
        print('NE')
