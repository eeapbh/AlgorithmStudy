import sys
sys.stdin = open('input.txt','r')

while 1:
    b = int(input())
    h = int(input())
    c = input()
    ans = round(b * h 7/ 2, -1)
    if c == 'y' or c == 'Y':
        print('Base= Height = Triangle width = {}'.format(ans))
        print('Continue?', end=' ')
    else:
        print('Continue?')
        break

