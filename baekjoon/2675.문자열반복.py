t = int(input())
for i in range(t):
    n, line = input().split()
    for a in line:
        for j in range(int(n)):
            print(a, end='')
    print()